# C_loop

# 파이썬 제어문 - 반복문(Loop)

# 1. 반복문의 정의
# : 특정 코드를 여러 번 실행하도록 프로그램에 지시하는 구조

# 2. 반복문의 종류
# : for 반복문, while 반복문

# for 반복문
# : 시퀀스 자료형을 순회하여 각 요소에 대해 특정 코드를 반복하도록 구현

# cf) 시퀀스 자료형
#       : 순서가 있는 자료형
#       : 리스트, 튜플, 문자형

'''
for문의 기본 구조

for 변수 in 시퀀스:
    반복할 명령 (실행할 코드 블럭)
'''

numbers = [1, 2, 3, 4, 5]

for num in numbers: # numbers 리스트에서 요소를 하나씩 꺼내 num에 담기
    print(num) # for문의 실행문을 동작

print('for문 종료')

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.upper()) # 문자열자료.upper(): 해당 문자열을 대문자로 변환

# 특정 횟수만큼 반복
# : range() 함수
# - 연속된 숫자(정수)를 만들어주는 파이썬 내장 기능

# 1) range(n): 0부터 n-1까지 정수를 생성
for i in range(5):
    print(i)

# 2) range(n, m): n부터 m-1까지 정수를 생성
for i in range(1, 4):
    print(i)

# 3) range(n, m, o): n부터 m-1까지 정수를 생성 (o는 각 숫자의 간격)
for i in range(1, 10, 2):
    print(i)

# == 컬렉션 타입과의 for문 == #
# : 리스트, 튜플, 딕셔너리
numbers = [1, 2, 3, 4, 5] # 리스트
for number in numbers:
    print(number)

numbers = (1, 2, 3, 4, 5) # 튜플
for number in numbers:
    print(number)

# 딕셔너리 사용 for문

# cf) 딕셔너리 활용 기능
# 1) .items(): 딕셔너리의 모든 키-값 쌍을 반환하는 기능
# 2) .keys(): 키를 모두 반환
# 3) .values(): 값을 모두 반환

fruitColors = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

# === .items() 사용시 ===
# 첫 번째 키를 fruit 변수에
# , 두 번째 값을 color 변수에 할당하여 사용

# cf) 딕셔너리명만 in 연산자에 사용하는 경우 key만을 반환
for fruit, color in fruitColors.items():
    print(f'The color of {fruit} is {color}')