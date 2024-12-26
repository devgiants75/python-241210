# F_practice

# 리스트 메서드 예제 #

# 문제 1: 주어진 리스트 numbers에 숫자 5를 추가하고
# , 결과 리스트를 출력하세요.
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers) # [1, 2, 3, 4, 5]

# 문제 2: 주어진 두 리스트 list1과 list2를 연결하고
# , 결과 리스트를 출력하세요.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) # [1, 2, 3, 4, 5, 6]

# 문제 3: 주어진 리스트 fruits의 두 번째 위치(인덱스: 1)에 'banana'를 삽입하고
# , 결과 리스트를 출력하세요.
fruits = ['apple', 'orange', 'grape']
fruits.insert(1, 'banana')
print(fruits) # ['apple', 'banana', 'orange', 'grape']

# 문제 4: 주어진 리스트 numbers에서 마지막 항목을 제거하고
# , 제거된 항목과 결과 리스트를 출력하세요.
numbers = [1, 2, 3, 4, 5]
removed_item = numbers.pop()
print(numbers) # [1, 2, 3, 4]
print(removed_item) # 5