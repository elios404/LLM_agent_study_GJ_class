# %%
# 환경 변수 로드를 위한 라이브러리 임포트
from dotenv import load_dotenv
load_dotenv()

# %%
# 필요한 타입 및 클래스 임포트
from typing_extensions import List, TypedDict, Literal
from langchain_core.documents import Document
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

# %%
# State 정의: LangGraph에서 노드 간에 전달될 데이터 구조
class ReqState(TypedDict):
    """
    요구사항 명세서 생성을 위한 상태를 정의하는 TypedDict입니다.
    각 필드는 요구사항의 여러 측면을 리스트 형태로 저장합니다.
    """
    req_actor: List[str]
    req_names: List[str]
    req_purpose: List[str]
    req_importance: List[str]
    req_level: List[str]
    req_function: List[str]
    req_process: List[str]
    # 비기능 요구사항 필드도 포함하여 확장성을 유지합니다.
    req_screen: List[str]
    req_security: List[str]
    req_perform: List[str]
    req_data: List[str]

# %%
# LLM과 Embedding 모델, Vector Store 설정
# OpenAI의 text-embedding-3-large 모델을 사용하여 임베딩 생성
embedding = OpenAIEmbeddings(model='text-embedding-3-large')
# Chroma DB를 사용하여 벡터 스토어 설정 및 Retriever 생성
vector_store = Chroma(
    collection_name='req-tax',
    embedding_function=embedding,
    persist_directory='../req-tax'
)
retriever = vector_store.as_retriever(search_kwargs={'k':3})

# gpt-4o 모델을 사용하여 ChatOpenAI 인스턴스 생성
llm = ChatOpenAI(model='gpt-4o')


# %%
# LLM의 구조화된 출력을 위한 Pydantic 모델 정의
class RequirementDetails(BaseModel):
    """
    LLM으로부터 구조화된 형태로 요구사항 세부 정보를 받기 위한 Pydantic 모델입니다.
    각 필드는 생성될 요구사항의 항목에 해당합니다.
    """
    req_level: Literal["상","중","하"] = Field(description="요구사항의 구현 난이도. 반드시 [상, 중, 하] 중 하나로 평가해주세요.")
    req_importance: Literal["상","중","하"] = Field(description="요구사항의 비즈니스적 중요도. 반드시 [상, 중, 하] 중 하나로 평가해주세요.")
    req_function: str = Field(description="개발에 필요한 기능 요구사항. 10줄 이하로 간결하게 작성해주세요.")
    req_process: str = Field(description="사용자와 시스템 간의 상호작용 흐름을 순서대로 작성해주세요. (예: 1. (사용자) '버튼' 클릭 ...)")

# %%
# 통합된 프롬프트 템플릿 정의
# 여러 정보를 한 번에 요청하여 LLM 호출 횟수를 줄입니다.
combined_prompt_template = """
당신은 IT 기업의 10년차 에이스 기획자입니다. 주어진 정보를 바탕으로 다음 4가지 항목을 명확하고 구체적으로 작성해주세요.

1.  **난이도**: 요구사항의 구현 난이도를 [상, 중, 하] 중에서 평가해주세요. 설명을 붙이지 마세요. 반드시 [상, 중, 하] 중 하나를 선택해서 그것만 반환하세요.
2.  **중요도**: 요구사항의 비즈니스적 중요도를 [상, 중, 하] 중에서 평가해주세요. 설명을 붙이지 마세요. 반드시 [상, 중, 하] 중 하나를 선택해서 그것만 반환하세요.
    (예시: "상", "중", "하")
3.  **기능 요구사항**: 개발에 필요한 핵심 기능들을 10줄 이하로 간결하게 요약해주세요.
4.  **프로세스 요구사항**: 사용자(또는 액터)와 시스템 간의 상호작용 흐름을 순서대로 작성해주세요. 
    출력 형태는 반드시 예시의 형태로 고정하세요. 1. 2. 와 같이 순서를 통해 프로세스를 정리하세요. 
    (예시: 1. (사용자) '지갑 연결하기' 버튼 클릭 -> 2. (시스템) MetaMask 팝업 실행 -> ...)

**주어진 정보:**
- **관련 정보 (Information):** {req_info}
- **액터 (Actor):** {actor}
- **요구사항 명 (Name):** {name}
- **요구사항 목적 (Purpose):** {purpose}
"""

# %%
# 모든 요구사항 세부 정보를 한 번에 생성하는 통합 노드 함수
def generate_requirement_details(state: ReqState) -> ReqState:
    """ 
    주어진 state를 기반으로 각 요구사항에 대한 난이도, 중요도, 기능, 프로세스를 한 번에 생성합니다.
    LLM 호출을 최소화하여 효율성을 높입니다.
    
    Args:
        state (ReqState): req_actor, req_names, req_purpose가 포함된 초기 상태
        
    Returns:
        ReqState: 생성된 세부 요구사항(level, importance, function, process)이 추가된 최종 상태
    """
    # 결과를 저장할 리스트 초기화
    levels, importances, functions, processes = [], [], [], []

    # Pydantic 모델을 사용하여 LLM이 구조화된 출력을 반환하도록 설정
    structured_llm = llm.with_structured_output(RequirementDetails)
    
    # 통합 프롬프트 템플릿으로부터 ChatPromptTemplate 생성
    prompt = ChatPromptTemplate.from_template(combined_prompt_template)
    
    # 프롬프트와 LLM을 연결하여 체인 구성
    chain = prompt | structured_llm

    # 입력 state에서 요구사항 목록 가져오기
    req_actors = state["req_actor"]
    req_names = state["req_names"]
    req_purposes = state["req_purpose"]

    # 각 요구사항에 대해 반복 처리
    for actor, name, purpose in zip(req_actors, req_names, req_purposes):
        # Retriever를 사용하여 관련 정보 검색
        req_info = retriever.invoke(name)
        
        # 단일 LLM 호출로 모든 세부 정보를 한 번에 생성
        details = chain.invoke({
            "req_info": req_info,
            "actor": actor,
            "name": name,
            "purpose": purpose
        })
        
        # 생성된 결과를 각 리스트에 추가
        levels.append(details.req_level)
        importances.append(details.req_importance)
        functions.append(details.req_function)
        processes.append(details.req_process)

    # 최종적으로 업데이트된 state 딕셔너리 반환
    return {
        "req_level": levels,
        "req_importance": importances,
        "req_function": functions,
        "req_process": processes,
    }

# %%
# StateGraph 빌더 생성 및 노드 추가
graph_builder = StateGraph(ReqState)

# 단일 노드로 모든 작업을 처리하도록 설정
graph_builder.add_node('generate_requirement_details', generate_requirement_details)

# %%
# 그래프의 흐름 정의: 시작 -> 세부사항 생성 -> 끝
graph_builder.add_edge(START, 'generate_requirement_details')
graph_builder.add_edge('generate_requirement_details', END)

# %%
# 그래프 컴파일
graph_jy = graph_builder.compile()

print("리팩토링된 그래프가 성공적으로 컴파일되었습니다.")
print("이제 'graph_jy_refactored.invoke()'를 사용하여 실행할 수 있습니다.")
