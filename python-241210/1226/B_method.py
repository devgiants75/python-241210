# B_method

# 내장 함수(Built in Function) VS 메서드(Method)
# 1) 공통점
# - 특정 작업을 수행하기 위한 코드의 묶음
# - 하나의 키워드를 사용하여 해당 코드의 묶음을 실행

# 2) 차이점
# 내장 함수
# - 파이썬에서 기본적으로 제공하는 함수들
# - 특정 타입에 종속되지 않고 어디서나 사용 가능
# - 키워드(obj)로 사용
# cf) obj(object) - (표현할 수 있는) 데이터
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 5 - iterable 길이 구하기: len()
print(type(numbers)) # <class 'list'> - 데이터 타입 구하기: type()
print(type('hello')) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(100)) # <class 'int'>

# 메서드
# - 특정 데이터 타입에 종속됨
# - 메서드를 호출(사용)하기 위해서는 반드시 해당 타입의 데이터가 필요
# - 데이터 타입에 따라 사용할 수 있는 메서드가 다름
# - A데이터타입.해당타입에서만 쓸 수 있는 메서드()
#       .마침표가 해당 타입에서 쓸 수 있는 메서드를 연결
text = 'hello'
print(text.upper()) # HELLO
num = 123
# print(num.upper())
# - 정수형의 데이터 타입은 upper() 속성(기능)을 가지고 있지 X