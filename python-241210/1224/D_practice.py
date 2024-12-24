# D_practice

# 1. 길이 구하기
# 길이: length - len()함수
length = len([1, 2, 3, 5, 5, 7, 8, 3, 9, 4])
print(length) # 10

# 최댓값과 최솟값 구하기: max(), min()
numbers = [4, 7, 2, 9, 1, 5]
max_value = max(numbers)
min_value = min(numbers)
print(max_value, min_value) # 9 1

# 정렬(오름차순, 내림차순)
unsorted_list = ['banana', 'orange', 'apple', 'cherry']
sorted_list = sorted(unsorted_list)
print(sorted_list) # ['apple', 'banana', 'cherry', 'orange']

# 모든 요소의 합 구하기: sum()
list_sum = sum([534, 232, 151, 123, 632])
print(list_sum) # 1672

# 0부터 10까지 숫자를 포함하는 리스트 생성: range()
range_list = list(range(0, 11))
print(range_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]