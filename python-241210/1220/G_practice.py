# G_Practice

# 반복문 + 조건문 예제

# 게임 시스템 개발
# - 로그인(1), 회원가입(2), 게임시작(3), 게임종료(0)

while True:
    print('로그인: 1 \n회원가입: 2 \n게임시작: 3 \n게임종료: 0')
    user_input = input('숫자를 입력해주세요.')

    # 숫자가 아닌 경우: 다시 입력 받기
    if not user_input.isdigit():
        # 변수.isdigit()
        # : 해당 변수의 값이 정수 O - True
        # : 해당 변수의 값이 정수 X - False
        # not + False: True
        print('숫자만 입력해주세요.')
        continue

    # 숫자를 입력한 경우
    number_input = int(user_input)

    if number_input == 1:
        print('로그인합니다.')
    elif number_input == 2:
        print('회원가입합니다.')
    elif number_input == 3:
        print('게임을 시작합니다.')
    elif number_input == 0:
        print('게임종료')
        break
    else:
        print('잘못된 선택입니다. 다시 입력해주세요.')