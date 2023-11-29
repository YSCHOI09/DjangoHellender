def desc():
    sv1=float(input("키 입력:"))
    sv2=float(input("몸무게 입력:"))
    sv3=input("현재 신체 활동 수준 입력:")
    sv4=input('운동 선호:')
    sv5=input('운동 목적:')
    sv6=input('하루 운동 선호 시간:')
    sv7=input('일주일간 운동 선호 횟수:')
    sv8=input('운동 장소 선호:')
    sv9=input('건강 상태:')
    sv10=input('오늘의 일기:')

    input_text=f"""
    <설문지>
    1. 키: {sv1}
    2. 몸무게: {sv2}
    3. 현재 신체 활동 수준: {sv3}
    4. 운동 선호 :{sv4}
    5. 운동 목적 :{sv5}
    6. 하루 운동 선호 시간 :{sv6}
    7. 일주일 운동 선호 횟수:{sv7}
    8. 운동 장소 선호 :{sv8}
    9. 건강 상태 :{sv9}
    <오늘의 일기>
    {sv10}
    """
    return input_text

