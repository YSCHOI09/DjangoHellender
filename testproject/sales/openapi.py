import os 
import openai
from desc import desc
import rec_ac
import re


result=desc()
openai.api_key='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'
messages=[]


content=f'''

{result}

이 <설문지> 와 <오늘의 일기>를 토대로 
1. 추천 운동 3개 ==> 각 운동에 대해서 설명 안해도 되고 운동 이름만 말해줘
2.식단표 아침,점심,저녁
3.스트레스 해소 방법중 추천해주고 싶은 차 종류 1개 와 운동 1개 ==> 차 와 운동에 대해서 설명 안해도 되고 차 이름 과 운동 이름만 말해줘
4.<설문지>와<오늘의 일기>에 대한 피드백
알려줄래?
정확히 
1. 추천 운동 3개: 
- 추천 운동1: 
- 추천 운동2: 
- 추천 운동3: 

2. 식단표:
- 아침: 
- 점심: 
- 저녁: 

3. 스트레스 해소관련 추천 차 종류 와 추천운동: 
- 추천 차 종류: 
- 추천 운동: 

4. <오늘 하루> 피드백


이런 형식과 동일하게 알려줘.
'''

messages.append({"role":"user","content":content})

completion=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

chat_response=completion.choices[0].message.content
print(f'ChatGPT:\n{chat_response}')
messages.append({"role":"assistant","content":chat_response})
print()
#운동 추천 Feedback
Feedback1=rec_ac.rec_ac(chat_response)
print("운동 3가지 종류\n")
print(Feedback1)
print()
#식단 추천 Feedback
Feedback2=rec_ac.rec_fd(chat_response)
print("아침 점심 저녁 식단\n")
print(Feedback2)
print()
#오늘의 피드백
Feedback3=rec_ac.rec_pd(chat_response)
print("오늘의 피드백\n")
print(Feedback3)
print()
Feedback4=rec_ac.rec_ta(chat_response)
print("스트레스 해소 차,운동\n")
print(Feedback4)

file_path='rec_ac1.txt'

with open(file_path,'w',encoding='utf-8') as file:
    file.write(f'{Feedback1[0]}\n')
    file.write(f'{Feedback1[1]}\n')
    file.write(f'{Feedback1[2]}\n')


#git init 
#git remote add origin [github repository 주소]
#git add .
#git commit -m "설명"
#git branch -M main
#git push origin main

