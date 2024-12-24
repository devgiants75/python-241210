# B_inner02

# 파이썬 내장 함수
# 2. 숫자형 내장 함수

# 1) abs(x): absolute value(절댓값)
# - 숫자의 절대값을 반환(부호X), x자리에 정수 또는 실수
print(abs(-5)) # 5
print(abs(+3.14)) # 3.14

result = abs(-5) - abs(+3) # 5 - 3
print(result) # 2

# 2) divmod(a, b): a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(14, 4)) # (3, 2) - (몫, 나머지)

# cf) 튜플(tuple)
# : 변경이 불가한 컬렉션 자료형

#!! 3) float(), int(): 문자열 또는 숫자를 실수, 정수로 변환
print(float(3)) # 3.0
print(int(3.14)) # 3

#!! 4) max(), min()
# : 여러 개의 데이터를 담는 자료형 중에서 가장 큰 값을 반환
# - iterable한 자료형에서 쓰임

# cf) iterable 자료형
# : 반복 가능한
# - string, list, tuple, set, dic 등
print(max([1, 5, 3, 4, 7])) # 7
print(min((1, 5, 3, 7, 4))) # 1

# 5) pow(a, b): a의 b 제곱한 결과를 반환
print(pow(2, 3)) # 8

# 6) round(number, N): 숫자를 N 소수점 자리까지 반올림한 결과를 반환
# - N은 생략 시 기본값 0을 가짐
print(round(3.14159)) # 3
print(round(3.14159, 2)) # 3.14

#!! 7) sum(iterable, start): iterable의 모든 항목과 시작값을 더한 결과를 반환
numbers = [1, 2, 3, 4, 5]
print(sum(numbers, 0)) # 15
print(sum(numbers)) # start 값 생략 가능
print(sum(numbers, 10)) # 25