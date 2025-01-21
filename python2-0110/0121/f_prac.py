# f_prac.py

### 예외 처리 예제 ###

#! 1. 이름 길이를 체크하는 예외 처리
# : 사용자로부터 입력받은 이름이 2 ~ 4자 사이가 아니면
#   NameError 예외를 발생(부모클래스 Exception)
#   이름은 2 ~ 4자 사이로 입력해주세요. 라는 예외 메시지 출력

#? cf) 문자열의 길이 측정: len(문자열데이터)
class NameError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
try:
    name = '이승아'
    name_length = len(name)
    if name_length < 2 or name_length > 4:
        raise NameError('이름은 2 ~ 4자 사이로 입력해주세요.')
except NameError as e:
    print(e)
else:
    print(f'입력된 이름은 {name}입니다.')
    
### 사용자 정의 예외 - 비밀번호 검증 시스템 ###
# 비밀번호가 해당 조건을 만족시키지 않을 경우 예외 발생
# : 최소 8자 이상, 최소 하나의 숫자를 포함

#? 사용자 정의 예외
class PasswordError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
#? 비밀번호 검증 함수 구현
# 문자열.isdigit(): 해당 문자가 숫자인지 판별
# any(): 주어진 시퀀스 중 어느 하나라도 참인 경우 True 반환
def validate_password(password):
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise PasswordError('비밀번호는 최소 8자 이상, 최소 하나의 숫자를 포함')
    
try:
    # pwd = 'qwer123'
    # pwd = 'qwerasdf'
    pwd = 'qwer1234'
    validate_password(pwd)
    print('비밀번호가 성공적으로 설정되었습니다.')
except PasswordError as e:
    print(e)