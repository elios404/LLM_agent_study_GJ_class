from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# 여러 번 질문과 답변을 진행
def get_ai_response(messages):
    response = client.chat.completions.create(
        model='gpt-5-mini', 
        messages=messages,
    )
    return response.choices[0].message.content

messages = [
    {'role' : 'system', 'content' : '너는 사용자를 도와주는 상담사야'}

]

while True:
    user_input = input('사용자 : ')
    
    if user_input == 'exit':
        break

    messages.append({'role' : 'user', 'content' : user_input})
    ai_response = get_ai_response(messages)
    print('AI : ', ai_response)

    messages.append({'role' : 'assistant', 'content' : ai_response}) # ai의 답변도 같이 저장, 그러면 다음 질문에서 이것을 기반으로 답변을 생성한다.