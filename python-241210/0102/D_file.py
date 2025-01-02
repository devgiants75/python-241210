# D_file

### 파이썬 파일 입출력 ###

# 파일 입력: 기존의 파일 내용을 읽어 들이는 것
# 파일 출력: 기존 파일에 새로운 내용을 추가하거나 새로운 파일을 생성하는 것

# 1. 파일 열기
# : 실제로 어떤 파일을 열어보는 것 X
# : 입출력 작업을 진행할 파일을 지정하는 것
# - 파일의 입출력 모두 파일 열기 작업이 선행되어야 함

# 1) open() 함수 사용 - 파일 객체를 반환
# 파일 객체 = open(파일명, 모드)

# 1-1) 파일명: 입출력을 수행할 파일
# - 파일명만 작성
#       : 작성하는 파이썬 소스코드 파일(.py)과 동일한 경로에 존재
# ex) open('sample.txt')

# - 전체 경로를 지정하는 경우
#       : 파일이 다른 디렉터리(폴더)에 있는 경우
# ex) open('C:\python-1210\python-241210\example.txt')

# - 상대 경로 지정(./)
# : 현재 디렉터리를 기준으로 경로 지정
# : 해당 파일이 같은 디렉터리 폴더 안에 있는 경우

# - 상대 디렉터리 경로 지정(../)
# : 현재 디렉터리의 상위 폴더를 기준으로 경로 지정

# 1-2) 모드: 파일을 여는 목적
# 입력 r (read, 읽기) - 파일이 없을 경우 (오류), 파일이 있는 경우 (읽기)
# >> 입출력 모드를 생략하는 경우 기본적으로 r모드 설정

# 출력 w, a, x
# w (write, 쓰기): 파일 X (새로 생성), 파일 O (새로 생성)
# a (append, 추가): 파일 X (새로 생성), 파일 O (추가)
# x (exclusive, 배타적 추가): 파일 X (새로 생성), 파일 O (오류)

# 1-3) 파일의 종류
# 텍스트 파일 OR 바이너리 파일 (텍스트 파일을 제외한 모든 파일)
# t (text): 기본값
# b (binary): 바이너리 파일

# 모드와 파일의 종류 혼합
# r, w, a, x / t, b
# rt: 텍스트 파일 읽기 모드
# ab: 바이너리 파일 추가 모드

# 파일 닫기
# : close() 함수 사용
# 파일객체.close()

file = open('new_file.txt', 'wt') # 새 파일 생성
file.close()

# with 문
# : 파일을 열고 작업을 마친 후 자동으로 파일을 닫아주는 기능
# - close() 함수를 따로 사용하지 않아도 됨

# with open('파일명', '모드') as file객체명:
#   파일 처리 코드

with open('my_file.txt', 'wt') as file:
    print('my_file.txt 파일이 생성되었습니다.')









