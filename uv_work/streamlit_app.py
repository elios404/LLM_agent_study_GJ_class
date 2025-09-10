import streamlit as st
import pandas as pd
import os
import tempfile
from typing import List, TypedDict
from langgraph.graph import StateGraph
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

# 이 부분은 사용자 환경에 맞게 수정이 필요합니다.
# 예를 들어, .env 파일에서 API 키를 로드하는 부분을 포함할 수 있습니다.
from dotenv import load_dotenv
load_dotenv()

# 팀원들이 구현한 서브 그래프 모듈을 임포트합니다.
# 실제 파일 경로에 맞게 수정해야 할 수 있습니다.
# 예시:
from jy import graph_jy as jy_subgraph
from mj import graph_mj as mj_subgraph
from sj import graph_sj as sj_subgraph

# 경고: 이 예제 코드는 실제 서브 그래프 모듈을 사용하지 않고,
# Streamlit 앱을 실행하기 위한 더미 함수를 사용합니다.
# 실제 프로젝트에서는 위에 있는 주석 처리된 부분을 사용하고,
# 아래의 더미 함수들을 제거하세요.

class ReqState(TypedDict):
    req_actor: List[str]
    req_names: List[str]
    req_purpose: List[str]
    req_importance: List[str]
    req_level: List[str]
    req_function: List[str]
    req_process: List[str]
    req_screen: List[str]
    req_security: List[str]
    req_perform: List[str]
    req_data: List[str]


def generate_df(state: ReqState) -> ReqState:
    st.info("실행: 데이터프레임 및 CSV 생성 (generate_df)")
    df = pd.DataFrame({
        "시스템": state.get("req_actor", []),
        "요구사항 ID": [f"REQ-{str(i).zfill(3)}" for i in range(1, len(state.get("req_names", [])) + 1)],
        "요구사항명": state.get("req_names", []),
        "중요도": state.get("req_importance", []),
        "난이도": state.get("req_level", []),
        "요청목적": state.get("req_purpose", []),
        "기능 요구사항": state.get("req_function", []),
        "프로세스 요구사항": state.get("req_process", []),
        "화면 요구사항": state.get("req_screen", []),
        "보안 요구사항": state.get("req_security", []),
        "성능 및 용량 요구사항": state.get("req_perform", []),
        "데이터 요구사항": state.get("req_data", []),
    })

    # requirements.csv 파일 생성
    df.to_csv("requirements.csv", index=False, encoding="utf-8-sig")
    st.session_state['result_df'] = df  # 결과를 세션 상태에 저장
    return state

# LangChain 그래프 빌드
graph_builder = StateGraph(ReqState)
graph_builder.add_node("mj_agent", mj_subgraph)
graph_builder.add_node("jy_agent", jy_subgraph)
graph_builder.add_node('sj_agent', sj_subgraph)
graph_builder.add_node('generate_df', generate_df)

from langgraph.graph import START, END
graph_builder.add_edge(START, 'mj_agent')
graph_builder.add_edge('mj_agent', 'jy_agent')
graph_builder.add_edge('jy_agent', 'sj_agent')
graph_builder.add_edge('sj_agent', 'generate_df')
graph_builder.add_edge('generate_df', END)
app_graph = graph_builder.compile()

# Streamlit UI
st.title("IT 프로젝트 요구사항 분석기")
st.subheader("PDF 기획서를 업로드하여 요구사항을 자동으로 분석해 보세요.")

# PDF 파일 업로드 위젯
uploaded_file = st.file_uploader("기획서 PDF 파일을 선택하세요", type="pdf")

if uploaded_file:
    st.success("파일 업로드 완료!")
    
    if st.button("요구사항 분석 시작"):
        # 임시 파일에 PDF 저장
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        try:
            # LangChain PDF 로더 및 텍스트 분할
            pdf_loader = PyPDFLoader(tmp_file_path)
            pdf_docs = pdf_loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", " ", ""])
            texts = text_splitter.split_documents(pdf_docs)

            embedding = OpenAIEmbeddings(model='text-embedding-3-large')
            
            vector_store = Chroma(
                collection_name='req-tax',
                embedding_function=embedding,
                persist_directory='../req-tax'
            )
            
            # --- LangGraph 실행 ---
            st.write("분석을 시작합니다. 잠시만 기다려 주세요...")
            with st.spinner('분석 중...'):
                initial_state = {
                    "req_actor": [],
                    "req_names": [],
                    "req_purpose": [],
                    "req_importance": [],
                    "req_level": [],
                    "req_function": [],
                    "req_process": [],
                    "req_screen": [],
                    "req_security": [],
                    "req_perform": [],
                    "req_data": [],
                }
                final_state = app_graph.invoke(initial_state)
            
            st.success("분석 완료!")
            
            # 결과 데이터프레임 표시
            if 'result_df' in st.session_state:
                st.write("---")
                st.subheader("분석 결과")
                st.dataframe(st.session_state['result_df'])

                # CSV 다운로드 버튼
                csv_file = st.session_state['result_df'].to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
                st.download_button(
                    label="분석 결과 CSV 다운로드",
                    data=csv_file,
                    file_name='requirements.csv',
                    mime='text/csv',
                )

        except Exception as e:
            st.error(f"분석 중 오류가 발생했습니다: {e}")
        finally:
            # 임시 파일 삭제
            if os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)
            
# 초기 실행 시 또는 리로드 시 결과 데이터프레임이 있으면 다시 표시
if 'result_df' in st.session_state and not uploaded_file:
    st.write("---")
    st.subheader("마지막 분석 결과")
    st.dataframe(st.session_state['result_df'])
    
    csv_file = st.session_state['result_df'].to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.download_button(
        label="분석 결과 CSV 다운로드",
        data=csv_file,
        file_name='requirements.csv',
        mime='text/csv',
    )
