from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-5-mini', 
    #temperature=0.9, # gpt의 답변 다양성 변수 0(정확한 답변)~1(풍성한 답변)
    messages=[
        {'role' : 'system', 'content':'너는 유치원생이야. 유치원생처럼 답변해줘.'},
        {'role' : 'user', 'content' : '참새!'},
        {'role' : 'assistant', 'content' : '짹짹!'}, #few-shot을 제공
        {'role' : 'user', 'content' : '강아지!'},
        {'role' : 'assistant', 'content' : '멍멍!'}, #few-shot을 제공
        {'role' : 'user', 'content' : '오리!'}
    ]
)

print(response)
print("---------------")
print(response.choices[0].message.content)