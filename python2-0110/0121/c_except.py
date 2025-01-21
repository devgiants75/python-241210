# c_except.py

#! 1. if 조건문 예외 처리 (고전적인 예외 처리 방법)
# : 사용자로부터 두 개의 정수를 입력받아 나눗셈 구현
# > 파이썬은 나누는 값(a/b에서 b값)이 0일 수 없음

a = 10
b = 0
# result = a / b #? ZeroDivisionError: division by zero

if b == 0:
    print('0으로 나눌 수 없습니다.') # 0으로 나눌 수 없습니다.
else:
    print(a / b)
    
### 파이썬 예외의 종류 (파이썬 내장 예외) ###

# 1. BaseException
# : 최상위의 예외 클래스 (파이썬 내장 예외는 반드시! 해당 클래스를 상속!)
# > 주로 직접적 사용 X, 해당 클래스를 상속받는 자식 클래스를 사용

# 2. ValueError
# : 잘못된 값이 입력될 때 발생
# EX) 정수가 예상되는 곳에 문자열이 전달

# 3. TypeError
# : 잘못된 타입의 데이터 '연산' 시 발생
# EX) 숫자 대신 문자열을 더하려고 할 때

# 4. ZeroDivisionError
# : 0으로 나누려고 할 때 발생

# 5. SyntaxError
# : 프로그램의 문법이 잘못되었을 경우 발생
# EX) 들여쓰기, 괄호의 불일치, 오타 등

### 파이썬 예외 처리 방식 ###

# 1. 모든 예외를 처리하는 방식
# : 예외의 종류와 상관없이! 모든 예외를 처리
# >> 추천X, 가능한 특정 예외를 지정하여 처리하는 것을 권장

#? 모든 예외 처리 기본 형태
'''
try:
    코드 작성 영역
except:
    예외 발생 시 처리 영역
    >> 처리할 예외를 지정하지 X
'''

print('=== 모든 예외 처리 예시 ===')
try:
    a = int(input('정수를 입력하세요: '))
    b = 0
    print(f'{a} / {b} = {a / b}')
except:
    print('예외가 발생하였습니다.')
# >> 예외 발생 시점에 대한 파악이 어려움: 사용 권장 X

### 2. 특정 예외만 처리하는 방식 ###
# : except 절은 여러 개를 동시에 사용 가능
# > except 절 뒤에 처리할 예외명을 생략하면 예외의 종류와 상관없이 처리(모든 예외 처리)

print('=== 특정 예외 처리 예시 ===')
try:
    a = int(input('정수를 입력하세요: '))
    b = 0
    print(f'{a} / {b} = {a / b}')
except ZeroDivisionError as m1:
    print('예외가 발생하였습니다. (0으로 나눌 수 없습니다.)')
    print(m1) # division by zero
except ValueError as m2:
    print('예외가 발생하였습니다. (정수만 입력하세요.)')
    print(m2) # invalid literal for int() with base 10: 'd안녕'
except Exception:
    # Exception 예외
    # : '그 외의' 모든 예외를 처리하는 코드 (예상치 못한 문제 처리)
    print('기타 오류가 발생하였습니다.')
    
### 3. 예외 메시지를 처리 ###
# : 모든 예외는 기본적으로 예외 메시지를 내장
# : as 키워드 - except문의 예외 메시지를 가지고 올 수 있음

'''
예외 메시지 처리의 기본 형태
try:
    코드 작성
except 예외명 as 예외메시지명:
    예외 처리 영역 - 예외 메시지명으로 출력
'''

# 리스트: 순서 O, 중복 O, 변경 O
# > 리스트에 존재하지 않는 인덱스 번호 사용 시 IndexError 발생

arrays = [1, 2, 3, 4, 5]
# 리스트 요소 접근 방법: 리스트명[인덱스 번호]

# print(arrays[10]) # IndexError: list index out of range

try:
    arrays[10]
except IndexError as message:
    # IndexError가 가지고 있는 예외 메시지를 message 변수에 저장
    # : except 블럭 내에서 활용 가능
    print(message) # list index out of range