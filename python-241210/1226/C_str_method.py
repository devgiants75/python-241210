# C_str_method

# 1. 문자열 메서드
# format() 메서드
# : 문자열에 변수를 삽입 or 형식을 지정하는 데 사용
print('Hello, {}. I am {} years old'.format('이승아', 50))

# count() 메서드
# : 특정 문자나 문자열이 등장하는 횟수를 세는 데 사용
print('Hello, Python'.count('o')) # 2

# find() 메서드
# : 특정 문자나 문자열이 처음 등장하는 인덱스 위치를 반환
# - 없을 경우 -1을 반환
print('Hello'.find('l')) # 줄 복사: ctrl + d
print('Hello'.find('w')) # -1

# index 메서드
# : 특정 문자나 문자열이 처음 등장하는 인덱스 위치를 반환
# - 없을 경우 valueError가 발생
print('Hello'.index('l'))
# print('Hello'.index('w')) # ValueError: substring not found

# 문자열 변환 메서드(영어에만 해당)
print('HELLO python'.upper()) # 대문자로 변환
print('HELLO python'.lower()) # 소문자로 변환
print('HELLO python'.capitalize()) # 첫 글자만 대문자, 나머지는 소문자
print('HELLO python'.title()) # 각 단어의 첫 글자를 대문자, 나머지 소문자




