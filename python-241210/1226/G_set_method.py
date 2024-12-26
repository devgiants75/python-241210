# G_set_method

# 파이썬 세트 메서드
# - 순서X, 변경O, 중복X
# - 중괄호 {} 사용

# cf) 파이썬 리스트 - 순서O, 변경O, 중복O (대괄호 [])
#           튜플 - 순서O, 변경X, 중복O (소괄호 ())

fruit1 = {'apple', 'banana'}
fruit2 = {'banana', 'orange'}

# 1. 교집합: intersection()
result1 = fruit1.intersection(fruit2)
print(result1) # {'banana'}

# 2. 햡집합: union()
result2 = fruit2.union(fruit1)
print(result2) # {'apple', 'banana', 'orange'}

# 3. 차집합: difference()
result3 = fruit1.difference(fruit2)
result4 = fruit2.difference(fruit1)

print(result3) # {'apple'}
print(result4) # {'orange'}
