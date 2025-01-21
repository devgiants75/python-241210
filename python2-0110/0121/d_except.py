# d_except

### else & finally 문 ###

#! else문
# : try 블록에서 예외가 발생하지 않으면 처리되는 구문
# > 주로 정상적으로 코드가 실행되는 경우 수행할 작업을 정의
#? cf) 반드시! except 블록 다음에 위치!

#! finally 문
# : 예외 발생 여부와 상관없이 try 구문이 종료(마무리)될 때 항상! 실행

'''
try:
    코드 작성
except 예외명 as 변수명:
    예외 발생 시 처리 영역
else:
    예외가 없을 때 처리 영역
finally:
    언제나 실행되는 영역
'''

#! else문 예제
try:
    a = 10
    b = 10 # 값을 0 또는 0이 아닌 값으로 변경 시 로직이 달라짐!
    print(f'{a / b}')
except ZeroDivisionError as e:
    # exception의 앞글자를 따서 e 키워드를 주로 사용
    print(e)
else:
    print(f'결과는 {a / b}입니다.')
finally:
    print('프로그램을 종료합니다.')
    
#! finally문 예제
# file의 변수를 선언 None 값을 할당
file = None # None: 아무것도 들어있지 않음을 의미
try:
    file = open('file.txt', 'rt', encoding='utf-8')
    content = file.read()
    print(content)
except FileNotFoundError as m1:
    print(m1) # 읽어올 파일이 존재하지 않는 경우 발생 #? [Errno 2] No such file or directory: 'file2.txt'
except Exception:
    print('파일 오류') 
finally:
    if file: # file 객체가 정의되었는지 확인
        file.close()
        print('파일을 닫습니다.')
    else:
        print('닫을 파일이 없습니다.')