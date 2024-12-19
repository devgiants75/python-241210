# B_tuple

# Tuple 자료형
# : 리스트와 유사 + 차이점(내부 값의 변경이 불가)
# : 소괄호()를 사용하여 생성, 각 요소는 쉼표(,)로 구분

# 순서 O, 변경 X, 중복 O
# >> 추가, 수정, 삭제가 안 됨

# cf) immutable 자료형: 변경이 불가능한 자료형(내부 값, 요소를 변경할 수 없음)

# 1. Tuple 생성
tuple1 = () # 빈 튜플
tuple2 = (1, 2, 3) # 정수형 튜플
tuple3 = ('a', 'b', 'c') # 문자형 튜플
tuple4 = (1, 'a', 2.0) # 다양한 자료형의 혼합
tuple5 = (1, 2, (3, 4)) # 튜플 안에 튜플 (중첩 튜플)
tuple6 = (1, 1, 2, 3, 1) # 데이터의 중복 O

# cf) 튜플의 경우 단일 요소(1개의 값)를 가지는 튜플 생성 시
#       , 요소 뒤에 쉼표를 붙이는 것을 권장
single_element_list = [1]
single_element_tuple = (1,)
print(single_element_tuple) # 1

# 2. 튜플의 연산
# : 리스트와 동일 (+, *)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2) # (1, 2, 3, 4, 5, 6)
print(tuple1 * 2) # (1, 2, 3, 1, 2, 3)

# 3. 튜플의 활용
# cf) 리스트와 튜플의 경우 비슷한 체계를 가지고 있어 중복된 기능이 많음

# 1) 요소의 위치를 반환하는 기능: index()
tuple = (1, 2, 3, 4)
list = [1, 2, 3, 4]
print(tuple.index(3)) # 2 # 요소 3의 인덱스 번호
print(tuple.index(1)) # 0
# print(tuple.index(5)) # ValueError: 함수 안의 요소가 튜플 내에 없음!

print(list.index(3)) # 2

# 주어진 값과 일치하는 요소의 개수를 반환하는 기능: count()
tuple_many = (1, 2, 2, 3, 2, 3, 1, 2, 3)
print(tuple_many.count(2)) # 4
print(tuple_many.count(3)) # 3

print(list.count(2)) # 1

# 튜플의 길이 구하기
print(len(tuple_many)) # 9

# 튜플은 요소값을 변경할 수 없기 때문에!
#   , 값을 변경하는 내장함수(기능)이 없음!

# 중첩 튜플의 사용법 (리스트도 동일!)
fruits = (('사과', 'apple'), ('바나나', 'banana'), ('망고', 'mango'))

print(len(fruits)) # 3
print(fruits[0]) # ('사과', 'apple')
print(fruits[1])
print(fruits[2])

apple = fruits[0] # ('사과', 'apple')
print(apple[1]) # apple

print(fruits[0][1]) # apple