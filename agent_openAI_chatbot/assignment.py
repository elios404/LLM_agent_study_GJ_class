from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def get_ai_response(messages):
    response = client.chat.completions.create( # gpt에 요청이 발생한다
        model = 'gpt-5-mini',
        messages=messages
    )
    return response.choices[0].message.content

# system, user, assistant 의 역할을 잘 알기

messages = [
    {'role' : 'system', 'content' : '''너는 사람들의 다이어트를 돕는 영양사, 음식 전문가야. 음식에 대해서 건강과 다이어트의 관점에서 답변해줘. 
    그리고 반드시 과거 기록 assistant에 few-shot으로 준 템플릿 형태로 너무 길지 않게 답변해줘.'''},
    {'role' : 'user', 'content' : '바나나는 다이어트에 어때?'},
    {'role' : 'assistant', 'content' : '''바나나
다이어트 추천 : 추천
칼로리 : 약 100kcal (보통 크기 1개 기준)
영양소 : 식이섬유, 칼륨, 비타민 B6, 마그네슘. 식이섬유가 풍부해 포만감을 주며, 칼륨은 체내 나트륨 배출을 도와 붓기를 빼는 데 좋습니다.
언제 먹으면 좋은지 : 아침 식사 대용이나 운동 전후에 먹으면 좋습니다.'''},
    {'role' : 'user', 'content' : '계란 어떻게 생각하니?'},
    {'role' : 'assistant', 'content' : '''계란
다이어트 추천 : 추천
칼로리 : 약 77kcal (보통 크기 1개 기준)
영양소 : 단백질, 필수 아미노산, 비타민 D, 콜린. 양질의 단백질은 근육 생성과 유지에 필수적이며, 포만감을 오래 유지시켜 식욕 조절에 도움을 줍니다.
언제 먹으면 좋은지 : 아침 식사로 먹으면 하루 동안 과식을 막는 데 좋습니다.'''},
    {'role' : 'user', 'content' : '라면이 너무 먹고 싶어..'},
    {'role' : 'assistant', 'content' : '''라면
다이어트 추천 : 추천하지 않음
칼로리 : 약 500kcal (일반 라면 1봉지 기준)
영양소 : 포화지방, 나트륨. 포화지방은 높은 칼로리로 체중 증가를 유발하며, 다량의 나트륨은 부종과 고혈압의 원인이 됩니다.
언제 먹으면 좋은지 : 늦은 저녁이나 야식으로 절대 먹지 않아야 합니다.'''},
    {'role' : 'user', 'content' : '오늘은 감자탕 어때?'},
    {'role' : 'assistant', 'content' : '''감자탕
다이어트 추천 : 추천하지 않음
칼로리 : 약 700~900kcal (1인분 기준)
영양소 : 고지방(국물), 나트륨, 탄수화물. 진한 국물에 지방과 나트륨이 많아 다이어트에 매우 불리하며, 밥을 함께 먹으면 고칼로리 식사가 됩니다.
언제 먹으면 좋은지 : 밤에는 먹지 않는 것이 좋으며, 가능하면 국물을 적게 먹는 것을 권장합니다.'''},
    

]

def main():
    while True:
        user_input = input("사용자 입력(종료하려면 '종료' 입력) : ").strip()

        if user_input.lower() == '종료':
            break

        messages.append({'role' : 'user', 'content' : user_input})
        ai_response = get_ai_response(messages)
        print('AI : ', ai_response)

        messages.append({'role' : 'assistant', 'content' : ai_response})

if __name__ == "__main__":
    main()