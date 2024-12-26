# E_collection_method

# 리스트 메서드 #

# 1. 리스트.append(추가할 요소)
# : 리스트의 끝에 새로운 요소를 추가
animals = ['cat', 'dog']
animals.append('elephant')
print(animals) # ['cat', 'dog', 'elephant']

# 2. 리스트.extend(추가할 리스트)
# : 리스트의 마지막에 다른 리스트를 연결하여 확장
animals.extend(['tiger', 'lion']) # 각각의 요소로 삽입
animals.append(['tiger', 'lion']) # 하나의 요소로 삽입

print(animals) # ['cat', 'dog', 'elephant', 'tiger', 'lion', ['tiger', 'lion']]

# 3. 리스트.insert(특정위치, 새로운 요소)
# : 특정 위치(인덱스)에 새로운 요소를 삽입
animals.insert(1, 'rabbit')
print(animals)
# ['cat', 'rabbit', 'dog', 'elephant', 'tiger', 'lion', ['tiger', 'lion']]

# 4. pop()
# : 특정 위치의 요소를 제거, 해당 요소를 반환
removed_animal = animals.pop(1)
print(removed_animal) # rabbit
print(animals) # ['cat', 'dog', 'elephant', 'tiger', 'lion', ['tiger', 'lion']]

# 5. remove()
# : 리스트에서 첫 번째로 나타나는 특정 값을 제거
animals.remove('elephant')
print(animals) # ['cat', 'dog', 'tiger', 'lion', ['tiger', 'lion']]

# 6. 리스트.clear()
# : 모든 요소를 제거 - 빈 리스트 생성
animals.clear()
print(animals) # []