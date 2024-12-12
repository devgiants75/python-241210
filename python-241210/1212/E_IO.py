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