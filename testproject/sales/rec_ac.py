import re

# chat_response는 전체 텍스트라고 가정합니다.
def rec_ac(chat_response):
    exercise_section1 = re.search(r'1\. 추천 운동 3개:(.*?)(?=\d\.)', chat_response, re.DOTALL)

    # 추출된 부분 출력
    if exercise_section1:
        recommended_exercises1 = exercise_section1.group(1).strip()
        
    else:
        print("추천 운동 부분을 찾을 수 없습니다.")

    lines1 = recommended_exercises1.splitlines()

    rec_ac1 = []
    for line in lines1:
        # 각 운동 목록에 대해 ':'의 존재 여부 확인
        if ':' in line:
            result = line.split(': ')[-1].split(', ')[0]
            
            rec_ac1.append(result)
        else:
            rec_ac1.extend([exercise.strip() for exercise in line.split(',')])

    return rec_ac1

def rec_fd(chat_response):
    
    exercise_section2 = re.search(r'식단표(.*?)(?=\d\.)', chat_response, re.DOTALL)

    # 추출된 부분 출력
    if exercise_section2:
        recommended_exercises2 = exercise_section2.group(1).strip()
        
    else:
        print("추천 식단 부분을 찾을 수 없습니다.")

    lines2 = recommended_exercises2.splitlines()

    rec_f=[]
    for i in range(1,4):
        exercise_list2 = [exercise.strip() for exercise in lines2[i].split('\n')]
        first_menu=exercise_list2[0].split(': ')[1]
        
        exercise_list2=exercise_list2[1:]
        
        exercise_list2.append(first_menu)
        
        rec_f.append(exercise_list2)
    return rec_f

def rec_pd(chat_response):
    start_index = chat_response.find("4")
    end_index = chat_response.find("5.", start_index)  # 다음 항목의 시작 전까지 추출
    feedback_text = chat_response[start_index:end_index].strip()

    # 결과 출력
    return feedback_text

def rec_ta(chat_response):
    start_index1 = chat_response.find("3.")
    end_index1 = chat_response.find("4.", start_index1)  # 다음 항목의 시작 전까지 추출
    feedback_text = chat_response[start_index1:end_index1].strip()

    # 결과 출력
    
    lines3 = feedback_text.splitlines()
    re_st=[]
    for i in range(1,3):
        feedback_list = [exercise.strip() for exercise in lines3[i].split('\n')]
        feedback_list=feedback_list[0].split(': ')[1]
        re_st.append(feedback_list)
    return re_st

  