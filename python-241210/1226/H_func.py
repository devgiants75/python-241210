# H_func

# 파이썬 함수(Function, func)
# : 하나의 특정한 목적의 작업을 수행하기 위해서 독립적으로 구성된 '코드의 집합'
# : 특정한 값 x를 전달하면 반드시 특정한 값 y를 결과로 반환

# 파이썬 함수의 구성
# - 함수 정의: 함수를 새로 생성
# - 함수 인자(인수): 함수에 전달할 입력(input) - argument
# - 함수 매개변수: 인수를 받아서 저장하는 변수 - parameter
# - 반환값: 함수의 출력(output) - return
# - 함수 호출: 만들어진 함수를 실제로 사용하는 것

# 1. 함수의 정의(definition)
# : def 키워드를 사용하여 함수를 정의
# - 함수의 이름과 괄호 안에 파라미터를 명시
# - 함수의 본문(기능을 명시)은 콜론(:) 다음 들여쓰기 하여 작성

# 함수의 기본 형태
# : 매개변수와 반환값은 선택

'''
def 함수명(매개변수):
    실행할 코드
    return 반환값
'''

def greet():
    print('안녕하세요! 만나서 반갑습니다 :)')

# 함수 호출
# : 함수명 다음 ()괄호를 붙여 호출
# - 매개변수값이 존재하는 경우 사용할 인수를 소괄호 안에서 작성
greet()
greet()
greet()

# 2. 파라미터 & 인수 - 선택(필수X)
# 1) 인수 x
greet() # 안녕하세요! 만나서 반갑습니다 :)

# 2) 인수 o (한 개)
def christmas(message):
    print(f'Merry {message}')

christmas('Christmas') # Merry Christmas
# christmas('Christmas', 'Happy New Year')
# : 지정된 매개변수의 수와 전달하는 인수의 개수는 반드시! 같아야 함!

# 3) 인수 o (여러 개)
# : 파라미터와 인수를 ,(콤마)로 구분하여 나열
# - 콤마로 구분된 매개변수의 순서대로 값을 전달
def args(name, age, city='부산'):
    # 기본값 인수 사용
    # : 매개변수에 직접 값을 할당
    # - 값 전달 X: 기본값 사용
    # - 값 전달 O: 해당 인수값 사용
    print(f'이름은 {name}, 나이는 {age}, 도시는 {city}입니다.')

args('이승아', 30) # 이름은 이승아, 나이는 30 입니다.
args(28, '이승아') # 이름은 28, 나이는 이승아 입니다.

# 키워드 인수를 사용하면 값의 혼동을 줄임
args(age=28, name='이승아') # 이름은 이승아, 나이는 28 입니다.

# 기본 인수값을 수정
args('이승아', 29, 'Busan') # 이름은 이승아, 나이는 29, 도시는 Busan입니다.

# cf) 파라미터 - 매개변수: 전달되는 인수를 저장할 함수 내의 변수
#       아규먼트 - 인자(인수): 함수에 전달하는 실제 데이터 값

# 함수 명명 규칙
# : lower_snake_case 사용
# EX) 덧셈 기능의 함수: sum_input

# : 동사를 사용
# EX) 더하다: add, sum / 빼다: subtract / 먹다: eat 등

# cf) 변수명 - 명사를 사용

# 3. 함수의 반환값 - 선택 (필수X)
# : return 키워드를 사용하여 함수의 결과를 반환
# : 함수에서는 return를 만나면 함수의 실행이 종료, 값을 반환

# 두 숫자를 더한 결과를 반환하는 함수
def add(a, b):
    result = a + b
    return result

# 반환값 사용 시: 변수에 담아서 사용
print(add(1, 2)) # 3

result = add(2, 3)
print(result) # 5

# 여러 값 반환(다중 반환)
# : 튜플 형태로 반환
def min_max(numbers):
    min_result = min(numbers)
    max_result = max(numbers)
    return min_result, max_result

result = min_max([1, 2, 3, 4, 5])
print(result) # (1, 5)

# 조건문에 따른 다른 값 반환
def is_even(number):
    # even 짝수
    if (number % 2 == 0):
        return True
    else:
        return False

print(is_even(5)) # False
print(is_even(6)) # True

# return이 없는 함수
# : 호출이 완료되면 None(아무것도 없음)을 반환
# - 보통 함수 호출로 출력하는 경우 사용
def none_return(name):
    print(f'Hello {name}')

none_return('이승아') # Hello 이승아