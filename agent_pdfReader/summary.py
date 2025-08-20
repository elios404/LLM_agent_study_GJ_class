from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def summairze_text(file_path: str):
    client = OpenAI(api_key=api_key)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    system_prompt = f'''
너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 저자의 문제 인식과 주장을 파악하고, 내용을 요약하라.
작성해야하는 포맷은 다음과 같다.

# 제목

## 저자의 문제 인식 및 주장 (15문장 이내)

## 저자 소개

=============== 이하 텍스트 ===============
{text}
'''
    
    print(system_prompt)
    print("-----------------------------------------")

    response = client.chat.completions.create(
        model = 'gpt-5-mini',
        messages= [ 
            {'role' : 'system', 'content' : system_prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == '__main__':  #왜 이렇게 쓰는가? : 이 함수가 이 파일 안에서만 사용되도록, 다른 파일에서 불려 사용되지 못함.
    file_path = './agent_pdfReader/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.txt'

    summary = summairze_text(file_path)
    print(summary)

    with open('./agent_pdfReader/output/summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)