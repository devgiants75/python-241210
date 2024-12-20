# D_loop

# 파이썬 제어문 - 반복문

# while문
# : 주어진 조건이 참(True)인 동안 실행할 명령을 반복
# >> 주어진 조건이 거짓이 될 때까지

# while문 내에는 주어진 조건을 거짓으로 만드는 코드를 작성!
# > 그렇지 않을 경우, 무한루프로 실행되어 프로그램의 효율성이 낮아짐

'''
while문 기본 구조

while 조건:
    실행할 코드(조건이 참인 동안에)
'''

# cf) 조건식에는 루프(반복)가 실행될지의 여부를 판단하는 boolean 타입의 표현식

count = 0
# 변수를 1씩 증가 시켜서 5보다 작을 때까지 출력
while count < 5:
    print(count)
    count += 1 # count = count + 1

# while True:
#     print('무한루프') # 파이썬 무한루프 종료 단축키: ctrl + f12

# break
# : 반복문을 즉시 종료 (무한 루프 종료)

# 10번 반복 - 0부터 9까지 range함수를 사용
# >> 해당 정수가 5가되면 종료

for i in range(10):
    if (i == 5):
        break
    print(i)

while True:
    user_input = input('종료하려면 q를 입력하세요: ') # q: quit
    if user_input == 'q':
        break

# continue
# : 현재 반복을 건너뛰고 다음 반복으로 넘어감
# - 루프의 현재 반복의 나머지를 중지, while문의 조건을 다시 확인
for i in range(10):
    # 0부터 9까지 반복
    if (i % 2 == 0):
        # 짝수 출력 X
        continue
    print(i) # 홀수 만 출력

# 중첩 for 문
# : 하나의 for문 안에 다른 for문이 포함되어 있는 구조
for i in range(3):
    # i: 0, 1, 2
    for j in range(2):
        # j: 0, 1
        print(i, j)

# 2차원 중첩 배열을 중첩 for으로 출력
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix: # 첫 번째 배열의 각 요소(배열)
    for number in row: # 내부 배열의 각 요소(숫자)
        print(number)