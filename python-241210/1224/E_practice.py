# E_practice

# === 쇼핑 리스트 만들기 === #
print('Christmas Shopping List')

# 쇼핑 리스트 만들기: 리스트(list)
shopping_list = ['wine', 'cheese', 'bread', 'strawberry jam', 'biscuit']

# 1. 쇼핑 리스트의 길이 구하기
print(f'1. 쇼핑 리스트 길이: {len(shopping_list)}') # 1. 쇼핑 리스트 길이: 5

# 2. 알파벳 순 정렬
print(f'2. 알파벳 순 정렬: {sorted(shopping_list)}')
# 2. 알파벳 순 정렬: ['biscuit', 'bread', 'cheese', 'strawberry jam', 'wine']

# 3. 쇼핑 리스트의 ID 리스트를 생성
# 첫 번째 아이템: 1부터 시작
# cf) 범위 값을 1부터 시작하여 리스트의 길이 + 1이 되기 전까지 1씩 증가하는 수를 생성
ids = range(1, len(shopping_list) + 1) # 1, 2, 3, 4, 5

# 4. ID와 쇼핑 리스트 품목을 결합: zip()
id_item_list = list(zip(ids, shopping_list))
print(f'3. ID와 품목 결합: {id_item_list}')
# 3. ID와 품목 결합: [(1, 'wine'), (2, 'cheese'), (3, 'bread'), (4, 'strawberry jam'), (5, 'biscuit')]