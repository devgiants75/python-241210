# F_practice

# pig.txt 파일을 열어서
# , 해당 텍스트 파일의 동요 가사에 '꿀'이라는 글자가
# , 몇 번 나오는지 찾는 예제 문제

# 1. 파일 열기
file = open('pig.txt', 'rt', encoding='utf-8')

# 2. 각 줄을 리스트로 저장
line_list = file.readlines()

# 3. 리스트의 반복을 통해 조건문에 '꿀'과 같은 글자가 있으면 count를 증가 할당
count = 0 # '꿀' 글자 수를 세기 위한 초기화

# > 17개의 줄 반복
# > 각 줄을 구성하는 각 문자를 순회
# > 조건문 사용

for line in line_list: # 17번 반복 (17개의 줄)
    for word in line: # 각 줄을 구성하는 각 문자 순회
        if word == '꿀':
            count += 1

# 4. 꿀은 전체 {count}번 나타납니다.
print(f'꿀은 전체 {count}번 나타납니다.')