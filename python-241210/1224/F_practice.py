# F_practice

# === 가위 바위 보 게임 === #

# 파이썬 내장 기능 random 모듈 사용

# cf) venv: virtual environment(가상 환경 생성 도구)
# - 파이썬 3.3 버전 이후 부터 표준 라이브러리에 포함
# - Python 프로젝트 영역과 별개로 다양한 기능을 포함

# cf) 모듈(module)
# : 관련된 데이터와 함수를 하나로 묶은 단위

# random 모듈
# : 임의의 값을 활용하는 다양한 데이터와 함수들이 포함
# random.choice(데이터)
# : 전달되는 데이터 내에서 random 모듈이 임의로 하나의 값을 선택하여 반환

# >> 사용 방법
# import 모듈명
# 모듈명.기능()

import random

# 가위 바위 보를 리스트(options)로 저장
options = ['가위', '바위', '보']

# '무한루프 내'에서 사용자로부터 가위, 바위, 보 중 입력 받기
while True:
    print('======================')
    print('가위, 바위, 보 게임을 시작합니다!')
    print('\'종료\'를 입력하면 게임이 종료됩니다.')
    user_choice = input('가위, 바위, 보 중 하나를 입력하세요.')

    # 사용자의 입력이 '종료'일 경우 게임을 종료(무한루프의 종료)
    if user_choice == '종료':
        print('게임을 종료합니다.')
        break # 반복문 종료

    # 사용자의 입력이 options 리스트에 없을 경우: 오류 메시지 출력 후 다시 조건 검사
    if user_choice not in options:
        print('잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력하세요.')
        continue # 이후의 코드를 읽지 않고 다시 반복문의 조건 검사

    computer_choice = random.choice(options) # options 리스트 내의 요소 중 하나의 값을 선택
    print(f'컴퓨터의 선택은 : {computer_choice}')

    # (사용자가) 이길 경우
    # 사용자 바위 - 컴퓨터 가위
    # 사용자 가위 - 컴퓨터 보
    # 사용자 보 - 컴퓨터 바위
    if (user_choice == '바위' and computer_choice == '가위') or \
            (user_choice == '가위' and computer_choice == '보') or \
            (user_choice == '보' and computer_choice == '바위'):
        # 긴 문장에서 문장의 가독성을 위한 줄바꿈 처리는 \ 역슬래시를 사용
        print('사용자의 승리입니다.')
    elif user_choice == computer_choice:
        # 비긴 경우
        print('무승부입니다.')
    else:
        # 지는 경우
        print('컴퓨터의 승리입니다.')