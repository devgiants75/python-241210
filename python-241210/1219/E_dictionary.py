# E_dictionary

# 딕셔너리(dictionary, dict)
# : 키(key)와 값(value)의 쌍으로 데이터를 저장하는 자료형

# 순서X - 삽입의 순서가 유지 (인덱스번호 X)
# 변경O
# 중복 - 키 중복 X, 값 중복 O

# 1. 딕셔너리 생성
# 1) 중괄호 {}로 표현, 각 항목은 콜론(:)으로 키와 값을 구분
#       - 각 요소는 콤마(,)로 구분

dict1 = {} # 빈 딕셔너리
dict2 = {'name': '이승아', 'age': 50, 'city': 'Busan'}

# 2) dict() 함수를 사용하여 생성
#       , 각 항목을 =로 구분

dict3 = dict(name='이도경', age=30, city='Busan')

print(dict2) # {'name': '이승아', 'age': 50, 'city': 'Busan'}
print(dict3) # {'name': '이도경', 'age': 30, 'city': 'Busan'}

# 2. 딕셔너리 활용
# 요소 추가/수정/삭제

# 딕셔너리의 값 추출(접근)
# : 딕셔너리명[키값]
print(dict3['name']) # 이도경

dict3['name'] = '이도경메롱'
print(dict3['name']) # 이도경메롱

# 요소 추가
# : 딕셔너리명['새로운키'] = 새로운 값
dict3['height'] = 169.2
print(dict3) # {'name': '이도경메롱', 'age': 30, 'city': 'Busan', 'height': 169.2}

# 요소 제거
# del 딕셔너리명['삭제하고자하는 키']
del dict3['city']
print(dict3) # {'name': '이도경메롱', 'age': 30, 'height': 169.2}