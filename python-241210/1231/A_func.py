# A_func

# func 키워드: function(함수)의 축약형

# 사칙 연산을 수행하는 함수를 작성 (+, -, *, /)
# : 각 함수에 파라미터 2개
# : 함수의 반환값을 1개

'''
def 함수명(파라미터들):
    함수 내의 동작
    return 반환값
'''

# add 함수: 두 수를 더하는 함수
def add(a, b):
    result = a + b
    return result

# substract 함수: 두 수를 빼는 함수
def substract(a, b):
    result = a - b
    return result

# multiply 함수: 두 수를 곱하는 함수
def multiply(a, b):
    result = a * b
    return result

# divide 함수: 두 수를 나누는 함수
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    else:
        result = a / b
        return result

# 4개의 함수 호출
# 함수명(인자값들)

# 인자값(인수) - 실제 함수 내에서 쓰일 데이터값
# 파라미터 - 함수 내에서 쓸 수 있도록 데이터를 저장하는 변수

print(add(10, 5))
print(substract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0)) # Error: Cannot divide by zero

# 줄 복사: ctrl + d, 실행: ctrl + shift + f10