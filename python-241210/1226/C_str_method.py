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

# strip() 메서드 + lstrip(), rstrip()
# : 문자열 양쪽 끝의 공백 및 특정 문자를 제거
message = '       Hello        '
print(message.strip() + "안녕")
print(message.lstrip() + "안녕")
print(message.rstrip() + "안녕")

# join() 메서드
# : '문자열 리스트'를 하나로 합쳐 하나의 문자열로 변환
# : 해당 요소들을 구분 짓는 문자(기호 포함)를 지정 가능
fruits = ['apple', 'orange', 'banana']

# 구분문자.join(연결할 리스트)
print(''.join(fruits)) # appleorangebanana
print(' '.join(fruits)) # apple orange banana
print(', '.join(fruits)) # apple, orange, banana

# split() 메서드
# : 하나의 문자열에서 문자열을 특정 문자(기호)를 기준으로 분리하여 리스트 생성
fruits = 'apple, orange, banana'
print(fruits.split(', ')) # ['apple', 'orange', 'banana']

# replace() 메서드
# : 특정 문자나 문자열을 다른 문자나 문자열로 교체
# : replace(a, b)
#   a 값: 변경할 문자, 문자열
#   b 값: 새로운 문자, 문자열
message = 'Hello World'
print(message.replace('World', 'Python')) # Hello Python