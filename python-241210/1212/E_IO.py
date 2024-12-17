# E_IO

# === 파이썬의 기본 입출력 === #

# 1. 출력
# 1) 기본 출력: print() 함수
print("파이썬의 기본 출력")

# cf) 이스케이프 문자: 문자열 내에서 특수한 의미를 가지는 문자 조합
# : \(백슬래시)로 시작 + 특정 문자
# \n: 줄바꿈
# \\: 백슬래시(\) 문자 그 자체
# \', \": 따옴표 문자 그 자체

# 1번
# Hello
# Python
print("Hello\nPython")

# 2번
# C:\python-1210\python-241210
print("C:\\python-1210\\python-241210")

# 3번
# 그가 말했다. "안녕"이라고
print("그가 말했다. \"안녕\"이라고")
print('그가 말했다. "안녕"이라고')

# +) print()함수에 여러 개의 데이터를 출력
# : 콤마(,)로 구분하여 나열
# >> 데이터 사이에 " " 한 칸 공백 지정
# >> (옵션) sep: 출력할 여러 값들 사이에 들어갈 문자를 지정, 기본값: 공백
print("Apple", "Banana", "Orange") # Apple Banana Orange
print("Apple", "Banana", "Orange", sep=", ") # Apple, Banana, Orange
print("Apple", "Banana", "Orange", sep=" & ") # Apple & Banana & Orange

name = "이승아"
job = "IT 강사"
hobby = "운동"
height = 169.2
print(name, job, hobby, height, sep=": ") # 이승아: IT 강사: 운동: 169.2

# 2) 포맷팅을 사용한 출력
# : 문자열 내에 변수나 값의 내용을 삽입하는 방법

# 1. %연산자 포맷팅
# : 문자열 내에 % 기호를 사용하여 특정 포맷 코드를 삽입해 해당 위체에 변수나 값을 삽입

# == 포맷 코드 ==
# %s: 문자열(모든 데이터 가능), %d: 정수, %f: 실수(부동 소수점 숫자)

# cf) %f: 사용하고자 하는 소수점 자리 수를 명시
#       - %.2f: 소수점 두 번째 자리까지

language = 'python'
print('Hello, %s' %language) # Hello, python

name = '이승아'
age = 50
# print('My name is %d' %name) - %d 포맷코드 위치에는 정수값만 들어올 수 있음!
print('My name is %s, I\'m %d years old' %(name, age)) # My name is 이승아, I'm 50 years old

# % 기호 그대로를 출력하고자 하는 경우
# : %% - % 기호 그대로를 사용
print('100% 유기농 우유')
print('100%%strawberry %s' %'딸기')

# %.Nf (N자리에 소수점 자리 수의 양의 정수가 들어감)
print('이승아의 키는 %.1f' %169.23456)

# %연산자 포맷팅은 여러 가지 타입의 포맷 코드를 사용, 순서와 값의 혼란이 가중되어 많이 쓰이지 않음!

# 2. format() 함수 사용
# : 문자열 내에 {}중괄호 자리에 값을 삽입하는 방법
print('Hello, {}'.format('이승아')) # Hello, 이승아
welcome_message = 'Hello, {}'.format('이도경')
print(welcome_message) # Hello, 이도경

print('{} {} {} {}'.format('I', "have", 4, "apples")) # I have 4 apples

# 'Python 3.6 버전 이상'에서는 f-string 사용을 권장!
# : 현대적인 문자열 포맷팅 형식
# - 중괄호 내에 직접적인 변수나 표현식을 넣어 쉽게 데이터 삽입
# - 표현식을 지원: 문자열 내에서 변수, 연산자 사용 가능
name = '이승아'
height = 169.2
print(f'My name is {name} and I am {height}cm tall') # My name is 이승아 and I am 169.2cm tall

a = 5
b = 3
print(f'Five times three is {a * b}') # 곱하기 * # Five times three is 15
# 줄 복사: ctrl + d
print(f'Five times three is {a} * {b}') # Five times three is 5 * 3

number = 7
print(f'다음 숫자는 {number + 1}입니다.') # 다음 숫자는 8입니다.

# f-string 소수점 자리 표현
# : 중괄호 내에 :(콜론)을 사용하여 포맷 지정
number = 3.14159
print(f'소수점 두 번째 자리: {number:.2f}') # 소수점 두 자리: 3.14
print(f'소수점 네 번째 자리: {number:.4f}') # 소수점 두 자리: 3.1416