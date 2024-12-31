# G_library

# 파이썬 표준 라이브러리

# === 라이브러리 ===
# : 파이썬 설치 패키지에 포함되어 있는 여러 기능을 제공하는 모듈과 패키지의 집합

# === 파이썬 표준 라이브러리의 종류 ===
# math: 수학적 함수, 상수 제공
# datetime: 날짜와 시간을 조작하는 기능을 제공
# random: 랜덤 숫자 생성 기능을 제공
# os: 운영체제와 상호작용하는 기능을 제공

# === 표준 라이브러리 사용 방법 ===
# import 하여 '모듈명.메서드()' 또는 '모듈명.속성'으로 사용

# 1. math 모듈
import math

# math.pi: 파이 - 원주율
print(math.pi) # 3.141592653589793
# math.sqrt(n): 제곱근
print(math.sqrt(16)) # 4.0

# cf) math 모듈의 함수들은 부동 소수점 자리를 반환
#       : 정수를 입력하더라도 무조건 소수점 자리를 반환

# math.fabs(): 절댓값
# math.factorial(n): 팩토리얼(!) - 해당 자연수 부터 1까지 1씩 감소하는 수를 모두 곱
# math.ceil(): 올림
# math.floor(): 내림

print(math.fabs(-5))
print(math.factorial(5)) # 5 * 4 * 3 * 2 * 1 == 120
print(math.ceil(2.3))
print(math.floor(2.7))

# 2. datetime 모듈
# : 날짜와 시간을 처리하는 기능
import datetime

# 현재 날짜 및 시간 가져오기
now = datetime.datetime.now()
print(now) # 2024-12-31 20:48:41.598192

# 날짜, 시간의 형식 지정
# date(날짜)
date = datetime.date(2025, 1, 1)
print(date) # 2025-01-01

# time(시간)
time = datetime.time(11, 7, 10)
print(time) # 11:07:10

