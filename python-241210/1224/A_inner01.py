# A_inner01

# 파이썬의 내장 함수 (Built-in Function)

# 내장 함수
# : 파이썬(프로그램)이 기본적으로 제공하는 함수(기능)
# - 별도의 라이브러리나 모듈을 설치 혹은 불러오지 않고도 사용 가능한 기능

# cf) 내장 함수는 데이터 타입별 혹은 기능별로 묶임

# 1. 문자열 내장 함수
# - chr() 함수: character 문자
# >> 문자 자신만이 가지는 코드 값을 반환 (유니코드)

# cf) 문자 코드
# : 프로그램이 인식할 수 있도록 문자를 숫자로 변형한 형태
# : 아스키코드(미국 표준 코드), 유니코드(국제 표준 코드)

print(chr(65)) # A
print(chr(97)) # a

# - ord() 함수: 문자를 유니코드로 반환
print(ord('A'))
print(ord('a'))
print(ord('ㄱ')) # 12593

# - eval() 함수: 실행하고자 하는 표현식을 전달하면 표현식의 결과값을 반환
print('100 + 200') # 100 + 200
print(eval('100 + 200')) # 300

# - isdigit: 문자를 전달하면 문자열이 숫자로 구성되어 있는지 확인
# 문자열데이터.isdigit()
# : 해당 문자열 데이터가 숫자로만 구성 - True / 그렇지 않으면 False 반환
print('123'.isdigit()) # True
print('123a'.isdigit()) # False

# - format() 함수: 전달받은 값과 포맷 코드에 따라 형식을 갖춘 문자열을 반환
print(10000) # 10000
print(format(1000000000, ',')) # 1,000,000,000

# format()의 포맷 코드
# 1) 천 단위 구분자: ','
# 2) 소수점 형식(고정된 자리수로 표현): '.Nf' (N은 자연수, 소수점 자리를 표현)
print(format(3.14159123123, '.3f')) # 3.142
# 3) 진수 표현: 다양한 진법으로 변환하는 방법
# - 2진수 표현: 'b' - binary
print(format(42, 'b')) # 101010
# - 16진수 표현: 'x' - hexadecimal(0 ~ 9 + a ~ f)
print(format(42, 'x')) # 2a

# - str() 함수: 전달받은 값을 문자열로 반환
print(str(10))
print(str(1.5))
print(str(True))

mix = str(10) + str(1.5) + str(True)
print(mix) # 101.5True