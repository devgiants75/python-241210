# D_set

# set
# : 순서 X, 변경 O, 중복 X

# cf) list: 순서 O, 변경 O, 중복 O - [] 대괄호
# cf) tuple: 순서 O, 변경 X, 중복 O - () 소괄호

# 1. set 자료형 생성
# : {} 중괄호를 사용하여 표현
# 1) {} 중괄호 사용 후 각 요소를 쉼표(,)로 구분
set1 = {1, 2, 3}

# 2) set() 함수를 사용하여 생성
set2 = set([1, 2, 3, 2, 3, 2]) # 리스트를 사용한 세트 생성
print(set2) # {1, 2, 3} # 중복 X

set3 = set('Hello') # 문자열을 사용한 세트 생성
print(set3) # {'e', 'H', 'o', 'l'} # 순서 X

# cf) set() 함수 내에 중복의 데이터나, 순서가 있는 데이터 삽입 시
#       중복 제거! 순서 제거! 하여 set의 요소로 전환

# cf) 순서가 없는 컬렉션 set은 인덱스 번호가 X
#       >> 인덱싱과 슬라이싱 등의 연산 지원 X

# 2. set의 활용
# 1) 요소 추가 & 제거
# 요소 추가: set명.add(추가값)
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(4) # 중복 불가! (오류 X)
print(my_set) # {1, 2, 3, 4}

# 여러 개 요소 추가: update(추가 데이터들)
my_set.update([4, 2, 1, 5])
print(my_set) # {1, 2, 3, 4, 5}

# 주어진 값이 있는 항목을 제거
# set명.remove(값)
my_set.remove(2)
print(my_set) # {1, 3, 4, 5}
# my_set.remove(6) # KeyError: 6 - 존재하지 않는 값 삭제 시 에러 발생

# set명.discard(값)
my_set.discard(3)
print(my_set) # {1, 4, 5}
my_set.discard(6)
print('정상적으로 실행됩니다.') # 정상적으로 실행됩니다.

my_set.clear() # 모든 요소를 제거 (컬렉션 타입 모두 사용)
print(my_set) # set()

# set 연산
# : 수학적 집합 연산이 가능

# 1. 합집합(union, | vertical bar) - union()
# 2. 교집합(intersection, & 앰퍼샌드) - intersection()
# 3. 차집합(difference, - 하이픈) - difference()
a = {1, 2, 3}
b = {3, 4, 5}

union_set = a | b # 합집합: a 또는 b에 포함되어 있으면 담기
intersection_set = a & b # 교집합: a 그리고 b에 모두 포함되어 있어야 담기
difference_set = a - b # 차집합: a에서 b를 제거
print(union_set) # {1, 2, 3, 4, 5}
print(intersection_set) # {3}
print(difference_set) # {1, 2}