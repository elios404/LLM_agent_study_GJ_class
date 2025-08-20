# pdf에서 불필요한 부분 제거하고 text로 추출하는 코드

import pymupdf
import os

pdf_file_path = './agent_pdfReader/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf'

doc = pymupdf.open(pdf_file_path) #pdf 파일 오픈, 문서 전체를 페이지 단위로 나눠 가져옴

# 헤더, 푸터 부분을 제외하고 텍스트 읽기 위해서
hearder_height = 80
footer_height = 80

full_text = ''

for page in doc:
    rect = page.rect # 페이지 크기 가져오기

    header = page.get_text(clip=(0,0, rect.width, hearder_height)) # 헤더 영역 (좌측 상단 x,y / 우측 하단 x,y) : 4개 값으로
    footer = page.get_text(clip=(0,rect.height - footer_height, rect.width, rect.height )) # 푸터 영역 

    text = page.get_text(clip=(0, hearder_height, rect.width, rect.height - footer_height)) #pdf 에서 텍스트 부분만 가져오기
    full_text += text + '\n -------------------------------------------------------\n' # 페이지별 구분선 

pdf_file_name = os.path.basename(pdf_file_path) # 경로에서 파일 이름.pdf 부분만 가져오기
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 파일이름.pdf를 . 기준 분리해서 .pdf 제외 파일 이름 부분만 가져오기

text_file_path = f"./agent_pdfReader/data/{pdf_file_name}.txt"
with open(text_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)