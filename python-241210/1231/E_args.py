# E_args

# args: arguments '여러 개 인자'의 축약어
# params: parameters '여러 개 파라미터'의 축약어

# 파이썬의 가변 인자

# 가변 인자
# : 개수가 변할 수 있는 인자
# - 임의의 개수를 받는 인자

def print_info(name, height):
    print(f'{name}의 정보 {height}')

# print_info('이승아', 169.2, 'enfj')
# : print_info() takes 2 positional arguments but 3 were given
# - 일반 인자의 경우 정의된 파라미터의 개수를 반드시 지켜 전달!

# 가변 인자의 표기법
# : 매개변수명 앞에 *표시를 붙임
# : 관례적으로 매개변수명을 args로 사용

# 가변 인자의 사용법
# : 함수 내에서 args 변수는 튜플로 처리

# cf) 튜플 - 순서 O, 변경 X, 중복 O (읽기 전용)
#       리스트 - 순서 O, 변경 O, 중복 O
#       셋 - 순서 X, 변경 O, 중복 X

def print_args(*args):
    # args 변수 - 튜플
    for arg in args:
        print(arg)

print_args('Hello', '안녕', '니하오', '오하이요', '새해 복 많이 받으세요')
print_args(1, 5, 3, 5, 2, 4, 3)

# 가변 인자를 받아 평균을 반환하는 함수 작성
# sum(), len() 내장 함수 사용 - iterable 타입

def average(*numbers):
    # 평균: 모든 데이터의 합 / 모든 데이터의 개수
    return sum(numbers) / len(numbers)

print(average(53, 12, 25, 32, 11)) # 26.6