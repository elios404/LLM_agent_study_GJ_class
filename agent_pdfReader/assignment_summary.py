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
너는 컴퓨터공학 분야의 정통한 연구자이자 교수야. 이번에 대학교에서 수업을 준비하면서 학생들에게 이해하기 쉽도록 논문을 요약하고 설명해 주고자 해.
아래 '이하 텍스트' 부분을 읽고 요약을 준비하려고 하고 있어.

학생들은 컴퓨터공학에 대한 지식이 깊지 않아. 그래서 논문에 대한 핵심은 짚으면서도 너무 어렵게 설명해서는 안돼.
또한 논문에 대한 요약이기에, 예시를 길게 들어서는 안돼고, 쉬운 언어로 짧게 요약해서 정리하는 것이 중요해.

그리고 주어진 텍스트의 아래는 마크다운으로 작성된 테이블 형태의 데이터가 있어. 이 부분은 위에 텍스트로 작성되어 있지만 테이블 형태로 알아보기 어려운 데이터를 명확하게 파악하기 위해서 작성되어 있어.


답변해야 하는 포맷은 다음과 같아.

# 논문 제목(영어) / 논문 제목 (한글)

## 논문의 문제 제기 및 목표 (5문장 이내)

### 배경 및 동기
### 연구 목표

## 제안된 방법론 또는 솔루션(15문장 이내)

### 핵심 아이디어
### 구현 방법

## 실험 및 결과 

### 실험 설정
### 핵심 결과

## 결론 및 시사점(5문장 이내)

### 연구의 기여
### 한계 및 미래 연구 

=============== 이하 텍스트 ===============
{text}
'''
    
    print(system_prompt)
    print("-----------------------------------------")

    response = client.chat.completions.create(
        model = 'gpt-5',
        messages= [ 
            {'role' : 'system', 'content' : system_prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == '__main__':  #왜 이렇게 쓰는가? : 이 함수가 이 파일 안에서만 사용되도록, 다른 파일에서 불려 사용되지 못함.
    file_path = './agent_pdfReader/data/04-NTCIR18-HIDDEN-RAD-ChoJ.txt'

    summary = summairze_text(file_path)
    print(summary)

    with open('./agent_pdfReader/output/summary2(assignment).md', 'w', encoding='utf-8') as f:
        f.write(summary)