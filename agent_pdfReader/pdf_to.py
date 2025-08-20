# pdf 파일에서 텍스트를 읽어오고 txt 파일로 저장하기

import pymupdf
import os

pdf_file_path = './agent_pdfReader/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf'

doc = pymupdf.open(pdf_file_path) #pdf 파일 오픈, 문서 전체를 페이지 단위로 나눠 가져옴

full_text = ''

for page in doc:
    text = page.get_text() #pdf 에서 텍스트 부분만 가져오기
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path) # 경로에서 파일 이름.pdf 부분만 가져오기
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 파일이름.pdf를 . 기준 분리해서 .pdf 제외 파일 이름 부분만 가져오기

text_file_path = f"./agent_pdfReader/output/{pdf_file_name}.txt"
with open(text_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)