### c_practice.py ###

#! VSCode는 파일 생성 시 
#   각 파일의 확장자를 반드시 작성!

import csv

# 초기 데이터
data = [
    ['Name', 'job', 'City'],
    ['이승아', '강사', '부산'],
    ['이도경', '회계', '부산'],
    ['김명진', '감리', '대전']
]

#? 파일 생성
file_name = 'practice.csv'
with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'{file_name} 파일이 생성되었습니다 :)')

# 특정 조건에 만족하는 데이터 필터링
# 예) 부산에 거주하는 사람 찾기
print('== 부산 시민 찾기 ==')
with open(file_name, 'rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) # 한 줄 건너뛰기: 제목 행 구분 (헤더 제거)
    for row in reader:
        if row[2].strip() == '부산': # strip(): 문자열 양쪽 공백 제거, 줄 바꿈 문자도 제거
            print(','.join(row)) # join(): 리스트의 요소를 문자열로 결합
            
#? csv 파일에 새로운 데이터 추가
new_data = ['조승범', '37', '경기']
with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(new_data)
    
print('새로운 데이터가 추가되었습니다 :)')