# H_practice

# 수학 퀴즈 게임
# : 사용자에게 랜덤으로 생성된 수학 문제(덧셈, 뺄셈, 곱셈)
# - 사용자가 정답을 입력하면 정답 여부를 알려줌

import random
import datetime

def generate_question():
    operations = ['+', '-', '*']
    selected_oper = random.choice(operations)

    # 두 개의 숫자를 랜덤으로 생성
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # 선택된 연산에 따라 정답 계산
    if selected_oper == '+':
        correct = num1 + num2
    elif selected_oper == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2

    question = f'What is {num1} {selected_oper} {num2}'
    return question, correct

def ask_question():
    # 사용자가 문제를 풀고 정답을 입력하는 함수
    question, correct = generate_question()

    print(question)
    start_time = datetime.datetime.now() # 문제 시작 시간 설정

    user_answer = int(input('Your answer: '))

    end_time = datetime.datetime.now() # 문제 종료 시간 설정

    # 시간 단위를 초단위로 계산
    # : .total_seconds() - 전체 시간을 초 단위로 계산
    time_taken = (end_time - start_time).total_seconds()

    if user_answer == correct:
        print(f'정답입니다! {time_taken}초 걸렸습니다.')
        return True, time_taken
    else:
        print(f'틀렸습니다! 정답은 {correct}입니다.')
        return False, time_taken

def play_math_quiz():
    # 게임을 무한 반복, 사용자에게 게임의 중단 여부를 확인
    continue_playing = True

    while continue_playing:
        correct, time_taken = ask_question()
        if not correct:
            # 정답이 아닌 경우
            continue

        # 정답인 경우
        print('Do you want to play again? (yes/no)')
        response = input().strip().lower() # 양쪽 공백 제거 & 소문자로 변경

        if response != 'yes':
            continue_playing = False

    print('게임을 종료합니다.')

play_math_quiz()