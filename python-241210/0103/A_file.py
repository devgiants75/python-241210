# A_file

# 파일 입출력
# open('파일명.확장자', '모드', 인코딩설정)함수
# : 파일에 대한 접근

# cf) 파일명 작성 - 입출력 작업을 수행할 파일 지정

# 1. 파일명만 작성하는 경우
# : 파이썬 소스 코드 파일(.py)과 동일한 경로(폴더)에 존재하는 파일
# - C:\python-1210\python-241210\0103 내의 'A_file.py' 파일
# - 작업하고 있는 파일과 동일한 0103 폴더 내의 파일만 가능

# 0103 폴더 내에 'example.txt' 파일 생성
open('example.txt')

# 0103 폴더 내에 'inner' 폴더 생성
# > 'sample.txt' 파일 생성

# open('sample.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'sample.txt'

# 2. 전체 경로를 지정하는 경우: 절대 경로
# - 파일 시스템에서의 전체 경로를 의미
# - 루트 디렉토리(폴더)부터 시작하여 파일이 위치한 곳까지 전체 지정
# - 파일 경로의 구분자는 열슬래시(\)

# C:\python-1210\python-241210\0103\inner\sample.txt
file = open('C:\\python-1210\\python-241210\\0103\\inner\\sample.txt', 'rt', encoding='utf-8')
# 이스케이프 코드: \\ (역슬래시 그 자체)

content = file.read()
print(content) # 파이썬1 종강일입니다 :)
file.close()

# 모드: r(읽기), w(쓰기), a(추가), x(배타적 추가)

# cf) 이스케이프 코드
# : 프로그래밍에서 사용할 수 있도록 미리 정의해 둔 문자 조합
# - 일반적인 문법과 충돌을 막기 위한 용도
# \n(줄바꿈, 개행), \" \'(따옴표 그 자체), \\(역슬래시 그 자체)

# 3. 현재 디렉터리(폴더)를 기준으로 경로를 지정: ./
# : 해당 파일이 같은 디렉터리 폴더에 존재하는 경우
# - 파일명만 작성하는 경우와 동일한 환경

# A_file.py를 기준으로 ./는 0103 폴더를 지정
# inner 폴더 위치: ...0103/inner
file = open('./inner/sample.txt', 'rt', encoding='utf-8')
content = file.read()
print(content) # 파이썬1 종강일입니다 :)
file.close()

# 4. 상위 디렉터리(폴더)를 기준으로 경로 지정: ../
# : 폴더를 벗어나는 방법
# - 상위의 폴더로 올라가는 방법

# A_file.py의 위치 - C:\python-1210\python-241210\0103
# 현재 디렉터리: 0103
# 상위 디렉터리: python-241210 내의 outer에 접근

file = open('../outer/text.txt', 'rt', encoding='utf-8')
while True:
    line = file.readline()
    if not line: break
    print(line)
file.close()