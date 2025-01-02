# E_practice

# 실습 문제

# === open()/close() 문 ===
# 1. 파일 sample.txt를 생성하고 다음 내용을 작성하세요
# 첫 번째 줄: "Hello, World!"
# 두 번째 줄: "Welcome to Python File I/O"

file = open('sample.txt', 'w', encoding='utf-8')
file.write('Hello, World!\n')
file.write('Welcome to Python File I/O\n')
file.close()

# 2. sample.txt 파일을 읽어 각 줄을 출력하세요.
file = open('sample.txt', 'r', encoding='utf-8')
for line in file:
    print(line.strip()) # 문자열.strip(): 문자열 양끝의 공백을 제거
file.close()

# 3. sample.txt 파일에 세 번째 줄 "This is a new line."을 추가하세요.
file = open('sample.txt', 'a', encoding='utf-8')
file.write('This is a new line.')
file.close()

# === with 문 ===
# 4. sample.txt 파일을 읽어 각 줄을 출력하세요.
with open('sample.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())