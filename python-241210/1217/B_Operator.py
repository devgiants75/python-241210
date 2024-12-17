# B_Operator

# 연산자(Operator)
# : 특정 작업을 수행하는 데 사용되는 특수 기호나 구문

# == 연산자의 종류 ==
# 항목의 개수
# - 단항(1, a, "안녕"), 이항(a = 1, message ="안녕")
# , 삼항 연산자(세 개의 항목으로 구분되는 연산자)로 구분

# '사용 목적'
# : 산술, 대입, 관계, 논리 연산자로 구분

# 1. 산술 연산자: 기본적인 수학 연산을 수행
# +, -, *, / (사칙연산)
# 거듭제곱(**), 몫(//), 나머지(%)
a = 5
b = 3
print(a + b) # 8
print(a - b) # 2
print(a * b) # 15
print(a / b) # 1.6666...
print(a ** b) # 125
print(a // b) # 1
print(a % b) # 2

# 대입 연산자 (할당 연산자)
# : 변수에 값을 할당하는 데 사용
# - 일반 대입 연산자: =
# - 복합 대입 연산자: +=, -=, *=, /=

a = 10 # 10을 a에 대입

a += 5 # a = a + 5
print(a) # 15

a -= 3 # a = a - 3
print(a) # 12

a *= 2
print(a) # 24

a /= 8
print(a) # 3.0 (나눗셈 연산 식 후의 값은 '실수(부동 소수점 자리 수)'로 반환)

# 3. 비교 연산자(관계 연산자)
# : 두 값의 관계를 비교하는 데 사용
# : 결과값이 boolean(논리) 타입으로 반환
# 이상(>=), 이하(<=), 초과(>), 미만(<)
# 동등(일치, ==), 부등(불일치, !=)
a = 10
b = 20

print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

# 4. 논리 연산자
# : boolean(참/거짓)의 값에 대한 논리적인 연산을 수행
# : and(논리곱), or(논리합), not(논리 부정)

a = True
b = False

# and(논리곱)
# : 모든 조건이 True일 때 True를 반환
# - False가 하나라도 존재하면 False를 반환
print('--- 논리곱 연산자 ---')
print(a and a and a and b and a) # False
print(a and a and a) # True

# or(논리합)
# : 적어도 하나의 조건이 True일 때 True를 반환
# : 모든 조건이 False 일 때만 False를 반환
print('--- 논리합 연산자---')
print(b or b or b or b or a or b) # True
print(a or a) # True
print(b or b) # False

# not(논리부정)
# : boolean값을 반전
print(not a) # False
print(not b) # True