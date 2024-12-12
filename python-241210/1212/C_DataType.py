# C_DataType

# 파이썬 (기본) 데이터 타입
# 기본 데이터 타입
# : 변수에 실제 데이터가 저장

# cf) 참조 데이터 타입
#       : 변수에 데이터가 저장된 주소가 저장

# 1. 숫자형(Number): 숫자를 나타내는 자료형
# - 정수(int, Integer), 실수(float)

# 1) 정수: 양의 정수, 0, 음의 정수를 포함
# 5, -3, 0 등

int_number = 1 # 줄 복사: ctrl + d (MacOS는 ctrl 대신 command)
int_number = -1
int_number = 0

# >> int(다른 타입 데이터) 함수: 다른 데이터 타입을 정수형으로 변환하는 기능
int_number = int(3.5)
print(int_number) # 3

int_number = int("7")
print(int_number) # 7

# print(int("안녕하세요"))
# : int() 내부에는 숫자로 변환 가능한 데이터만 작성
# >> 같은 숫자형 내의 데이터나 숫자 체계의 문자열 등

# 2) 실수: 소수점이 있는 숫자
# 3.14, -0.01, 2.0 등
float_number = 3.14
float_number = -0.01
float_number = 0.0

# float(): 정수나 문자열을 실수형으로 변환
print(float(3)) # 3.0
print(float("7")) # 7.0

# 2. 논리형 (Boolean, 불리언, bool)
# : 참(True)과 거짓(False)을 나타내는 자료형
# - True, False 두 가지 값만을 가짐
# - 시작을 대문자로 사용
bool_data = True # 참
bool_data = False # 거짓

# >> bool() 함수: 다른 데이터 타입을 bool 타입으로 변환
# - 각 데이터 타입 별 비워진 값(초기값): False
# - 그 외의 값은 모두: True

# cf) 데이터 초기값
# 숫자(0), 문자('', ""), None, [list 리스트]
#   , {set 셑, dictionary 딕셔너리}, (tuple 튜플)

print(bool(0)) # False
print(bool(''))
print(bool([]))
print(bool({}))

print(bool(2315646540)) # True
print(bool('가나다라마바사'))
print(bool([123]))
print(bool({123}))

# 3. 문자열 (string, str)
# : 문자, 단어 등으로 구성된 문자들의 집합
# : 작은따옴표 또는 큰따옴표로 묶어서 표현
str_data = "Hello"
str_data = "Python"

# >> str() 함수: 다른 데이터 타입을 문자열로 변환
print(str(100))
print(str(False))
print(str(True))
print(str(100.100)) # 100.1: 문자는 소수점 끝자리를 0으로 두지 않음