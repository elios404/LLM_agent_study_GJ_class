# %%
from dotenv import load_dotenv
load_dotenv()


# %%
from typing_extensions import List, TypedDict
from langchain_core.documents import Document
from langgraph.graph import StateGraph

class ReqState(TypedDict):
    req_actor: List[str] # 시스템
    req_names: List[str] # 요구사항명
    req_purpose: List[str]  # 요청목적
    req_importance: List[str] # 중요도
    req_level: List[str] # 난이도
    req_function: List[str] #기능 요구사항
    req_process: List[str] # 프로세스 요구사항
    req_screen: List[str] #화면 요구사항
    req_security: List[str] #보안 요구사항
    req_perform: List[str] # 성능 및 용량 요구사항
    req_data: List[str] # 데이터 요구사항     
    context: List[Document]
    

# %%
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o", temperature=0)
# generate_prompt = hub.pull("rlm/rag-prompt") 
actor_prompt = """ 
당신은 뛰어난 IT 프로젝트 기획자, 설계자이다.
주어진 프로젝트 기획서 context를 기반으로 요구분석을 진행하기 위한 사용자 그룹을 정의하라.
사용자 그룹 중 의미의 중복이 발생할 수 있는 사용자 그룹은 공통된 새로운 사용자 그룹을 정리하라.
사용자 그룹은 기획서를 기반으로 진행하라. 또한 실제 서비스 사용시에 발생할 수 있는 사용자 그룹만 정의하라.

예시 : "공통", "관리자", "사용자", "창작자" 등..

context : {context}
"""

generate_prompt = ChatPromptTemplate.from_template(actor_prompt)

# %%
from pydantic import BaseModel, Field
from typing import List

class Actor(BaseModel):
    actors : List[str] = Field(description="기획서를 기반으로 요구분석에서 등장할 수 있는 사용자 그룹들")

# %%
def generate_actor(state: ReqState) -> ReqState:
    structed_llm = llm.with_structured_output(Actor)
    chain = generate_prompt | structed_llm

    actors = chain.invoke({"context": state["context"]})
    
    print(actors.actors)
    
    return {"req_actor": actors.actors}


# %%
reqirement_prompt = """ 
당신은 뛰어난 IT 프로젝트 기획자, 설계자이다.
주어진 프로젝트 기획서 context와 사용자 그룹 actors를 바탕으로 요구사항 정의를 위한, 요구사항명 목록과 그 요구사항을 필요로 하는 사용자 그룹을 반환하라.
요구사항명은 각 그룹에서 발생할 수 있는 요구사항을 최대한 자세하고, 여러 유스케이스를 포함할 수 있도록 반환하라. 
요구사항명은 사용자가 서비스를 사용하면서 발생할 수 있는 경우들만 작성하라.
반드시 각각의 actors 그룹에서 최소 4개 이상의 요구사항을 반환하라.
요구사항명 뒤에 어떤 사용자 그룹의 요구사항인지 추가로 작성하라. 
이때 반드시 '#'를 구분자로 하여 사용자 그룹을 작성하라.

예시)
요구사항명 : 웹3 지갑을 이용한 회원 인증 (로그인/로그아웃)#공통
요구사항명 : 전역 네비게이션 바 (GNB) 및 푸터#공통
요구사항명 : 팬 콘텐츠 등록#창작자
요구사항명 : 광고 시청을 통한 무료 '응원권' 획득#사용자

context : {context}
actors : {actors}
"""

req_prompt = ChatPromptTemplate.from_template(reqirement_prompt)

# %%
class Require(BaseModel):
    names_with_actor : List[str] = Field(description="기획서, 사용자 그룹을 기반으로 나올 수 있는 요구사항명들#사용자 그룹")

# %%
def generate_names(state: ReqState) -> ReqState:
    """
    입력:  state["context"], state["req_actor"]
    출력:  {'req_names': <모든 액터의 요구사항명 합집합(중복 제거)>}
    설명:  액터(사용자/관리자/공통)별로 요구사항명을 추출한 뒤,
        전부 합쳐서(중복 제거) req_names에 넣어 반환합니다.
    """
    
    structed_llm = llm.with_structured_output(Require)
    chain = req_prompt | structed_llm
    
    requires = chain.invoke({"context": state["context"], "actors" : state['req_actor']})

    actors = []
    names = []

    for r in requires.names_with_actor:
        l = r.split("#")
        actors.append(l[1])
        names.append(l[0])
    
    print(actors)
    print(names)
    

    return {"req_actor": actors, "req_names" : names}


# %%
purpose_prompt = """ 
당신은 뛰어난 IT 프로젝트 기획자, 설계자이다.
프로젝트 기획서의 내용인 context와 요구사항명과 사용자 그룹이 합쳐진 requires 를 기반으로 각 요구사항의 목적을 반환하라.
반드시 **모든** requires에 대해서 1개의 요구사항 목적을 반환하라.

context : {context}
requires : {requires}

반환 예시 ) 
requires : 콘텐츠 및 창작자 검색 기능 -> 반환 : 사용자가 원하는 특정 콘텐츠나 창작자를 쉽게 찾을 수 있도록 하기 위함.
requires : 창작자 프로필 설정 및 관리 -> 반환 : 익명의 지갑 주소 대신, 창작자가 자신을 표현할 수 있는 고유한 프로필(닉네임, 이미지 등)을 설정하여 커뮤니티 내에서 정체성을 가질 수 있도록 하기 위함.


"""

pp_prompt = ChatPromptTemplate.from_template(purpose_prompt)

# %%
class Purpose(BaseModel):
    purpose : List[str] = Field(description="각각의 요구사항 명들에 대한 요구사항 목적")

# %%
def generate_purpose(state: ReqState) -> ReqState:
    """
    입력:  state["context"], state["req_names"]
    출력:  {'req_purpose': <req_names와 동일 길이의 목적 리스트>}
    설명:  req_names를 배치로 나누어 LLM에 질의, 결과를 순서대로 이어붙임.
    """
    input = [" / ".join([name, actor]) for name, actor in zip(state['req_names'], state['req_actor'])]
    
    structed_llm = llm.with_structured_output(Purpose)
    chain = pp_prompt | structed_llm
    
    purposes = chain.invoke({"context": state["context"], "requires" : input})

    return {"req_purpose": purposes.purpose}


# %%
from langgraph.graph import StateGraph, START, END

builder = StateGraph(ReqState)
builder.add_node("generate_actor", generate_actor)                 # 문서 전반 액터(참고)
builder.add_node("generate_names", generate_names)                 # 요구사항명
builder.add_node("generate_purpose", generate_purpose)             # 목적
# builder.add_node("classify_actor_per_item", classify_actor_per_item)  # 항목별 액터 분류(핵심)

builder.add_edge(START, "generate_actor")
builder.add_edge("generate_actor", "generate_names")
builder.add_edge("generate_names", "generate_purpose")
# builder.add_edge("generate_purpose", "classify_actor_per_item")    # 목적 생성 후, 목적+이름 기반으로 액터 분류
builder.add_edge("generate_purpose", END)

graph_mj = builder.compile()
