# A_random_game

import random

# 숫자 맞추기 게임
# : 1부터 20까지의 '임의의' 숫자를 선택
# - 기회는 총 5번 (5번 반복)

# random 모듈의 randint(a, b) 함수 사용
# : a와 b 사이의 정수 중 무작위 수를 추출

# 무작위 수 추출 (a와 b 사이의 정수)
secret_number = random.randint(1, 20)

# 게임 규칙 설명 메시지 출력
print('1부터 20사이의 숫자를 맞춰보세요. (기회 5번)')

# 사용자가 5번 시도할 수 있도록 반복문을 설정
for i in range(1, 6):
    print(f'{i}번째 시도: 숫자를 입력하세요.')
    guess = int(input()) # 사용자가 추측한 숫자를 입력받아 정수로 변환

    # 사용자의 추측과 컴퓨터가 가지고 있는 숫자를 비교
    if guess < secret_number: # 10인데 사용자 5를 입력한 경우
        print('정답보다 낮습니다. 더 큰 수를 입력해주세요.')
    elif guess > secret_number:
        print('정답보다 높습니다.')
    else:
        break # 반복문 내에서 break를 만날 경우 남은 반복 횟수와 상관없이 반복문이 종료!

# 사용자가 정답을 맞추었는지 확인
if guess == secret_number:
    print(f'축하합니다! {i}번 시도에 숫자를 맞추었습니다.')
else:
    print(f'기회를 모두 소진하였습니다. 정답은 {secret_number}입니다.')