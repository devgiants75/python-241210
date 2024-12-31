# D_practice

# 1. 'Hello, World!'를
# 출력하는 함수를 작성
def hello_world():
    print("Hello, World!")
hello_world()

# 2. 주어진 두 숫자의 합을 (3, 2)
# 반환하는 함수를 작성
def add(a, b):
    return a + b
print(add(3, 2))

# 3. 주어진 숫자 리스트의 합을 ([1, 2, 3, 4, 5])
# 반환하는 함수를 작성 - sum(리스트) 메서드: 해당 리스트의 모든 요소의 합을 반환
def sum_array(numbers): # numbers - 인자를 받아 저장하는 매개변수
    return sum(numbers)

print(sum_array([1, 2, 3, 4, 5])) # 15 - [1, 2, 3, 4, 5] 인자

# 4. 이름을 인자로 받아
# 인사하는 함수를 작성
# 만약 이름이 주어지지 않은 경우,
# "Guest"라는 이름으로 인사
def greet(name='Guest'): # name 변수가 비워질 경우 자동으로 Guest 기본값이 할당
    print(f'Hello, {name}')

greet('이승아') # Hello, 이승아
greet() # Hello, Guest