# F_collection_operator

# 컬렉션 자료형의 연산

# 1. 시퀀스(sequence) 연산자

# cf) 시퀀스(sequence) 자료형
# : 순서가 있는 자료형 (리스트, 튜플, 문자열)

# - 결합(+), 반복(*) 연산자
result1 = [1, 2, 3] + [4, 5, 6]
print(result1) # [1, 2, 3, 4, 5, 6]

result2 = (1, 2) * 3
print(result2) # (1, 2, 1, 2, 1, 2)

# 2. 멤버십 연산자
# : 특정 값이 시퀀스나 컬렉션에 속해 있는지 확인하는 데 사용
# 시퀀스 - 리스트, 튜플, 문자열
# 컬렉션 - 리스트, 튜플, 셋, 딕셔너리

# 1) in 연산자
# : 시퀀스나 컬렉션에 특정 요소가 포함 - True, 그렇지 않으면 - False
list = [1, 2, 3, 4, 5]
str = "Hello Python"

# 찾고자하는값 in 시퀀스또는컬렉션
print(3 in list) # True
print(6 in list) # False

# 2) not in 연산자
# : 시퀀스나 컬렉션에 특정 요소가 포함 - False, 그렇지 않으면 - True

print('Python' not in str) # False
print('Java' not in str) # True

# cf) 연산자의 우선순위
result = (3 + 4) * 2 ** 2 > 10
print(result) # True

# 1. 괄호 ()
# 2. 거듭제곱 **
# 3. 곱셈, 나눗셈, 나머지, 몫: *, /, %, //
# 4. 덧셈, 뺄셈

# 연산자 복습 문제 #
# BMI(체질량) 계산기 프로그램
# : 체중(kg)을 키(m)의 제곱으로 나눈 값

# 사용자로 부터 체중과 키를 입력받아 BMI를 계산하는 공식

weight = float(input('체중(kg)를 입력하세요: '))
height = float(input('키(cm)를 입력하세요: '))

# bmi = weight / 키 제곱값
bmi = weight / height ** 2

print('계산된 BMI', bmi) # BMI 0.0018556773222226112