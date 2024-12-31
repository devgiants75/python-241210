# B_scope

# scope(스코프)
# : 지역, 영역

# 파이썬의 '지역' 변수 VS '전역' 변수

# 1. 지역(Local) 변수
# : 특정 함수 또는 메서드 내부에서 선언된 변수
# : 함수 내에서 정의, 오직 그 함수 내에서만 접근 가능한 변수
# - 함수가 종료되면 그 변수의 생명 주기도 끝남

def my_function():
    local_variable = 5 # 지역 변수 선언 - 함수 내에 종속 O
    print(local_variable)

# 지역 변수 데이터 출력(함수 호출)
my_function() # 5
# print(local_variable) # Unresolved reference 'local_variable'
# : 함수 외부에서는 지역 변수에 대해 접근 불가

basic_variable = 10 # 함수 내에 종속 X
print(basic_variable) # 10

# 2. 전역(global) 변수
# : 함수 외부에서 선언, 프로그램 전체에서 접근할 수 있는 변수
# - 함수 내부에서 전역 변수를 사용하려면 global 키워드를 사용해 선언
# - 전역 변수의 접근은 global 키워드 없이 사용 가능

global_variable = "전역 변수"

def my_function2():
    # 전역 변수의 값을 참조(가져옴)
    print(global_variable)

my_function2() # 전역 변수
print(global_variable) # 전역 변수

# global 키워드
# : 함수 내부에서 전역 변수의 값을 변경하고자 할 때
# - 해당 키워드 미지정 시 같은 이름의 새로운 지역변수가 생성

a = 0
# 전역 변수
# - 해당 변수를 지역 또는 전역에서 모두 활용 가능하도록 global 선언이 이루어져야 함
# - global 선언 위치: 사용하고자 하는 지역 내(함수 내)

def my_function3():
    # global 선언 전에는 새로운 지역 변수로 인식: 변수 선언부 확인 X
    global a
    a += 5
    print(a)

my_function3() # 5
print(a + 3) # 8
my_function3() # 10
print(a)

# 파이썬에서 전역 변수를 사용하기 전에는 (global 선언 전)
# , 반드시 해당 변수가 명시적으로 선언되어야 함