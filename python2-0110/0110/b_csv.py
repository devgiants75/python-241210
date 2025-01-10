### b_csv.py ###

#! CSV 파일
# : CSV(Comma Separeted Values) 파일
# : 쉼표로 분리된 값
# : 필드(데이터)를 쉼표로 구분한 파일, 표 형태의 데이터 저장에 활용
# - 열: 쉼표로 구분
# - 행: 새 줄로 구분

'''
이름,학년,반
이승아,1학년,3반
이도경,3학년,7반
'''

#? 1. 'with구문을 사용한' CSV 파일 읽기
# : 한 줄에 한 데이터 읽기: readline() 메서드로 한 줄씩 읽기
#   - 행의 데이터
# : 쉼표로 분리: split() 메서드로 분리
#   - 열의 데이터

import os
print(os.getcwd())

# 빈 리스트: 학생 정보를 저장할 리스트
student_list = []
 
with open('student.csv', 'rt', encoding='utf-8') as file:
    # file.readline(): 각 행을 분리하는 메서드(한 줄씩 읽음)
    while True:
        line = file.readline()
        if not line: # 라인이 끝날 경우: 모든 행을 읽은 경우
            break # while문 종료
        student = line.split(',')
        student_list.append(student) # 배열에 요소 추가: .append(요소)
        
print(student_list)

# 파이썬 실행 단축키: ctrl + f5 (사용자 지정 단축키)

#? 1. 'csv 모듈을 사용한' CSV 파일 읽기
# : csv 모둘의 reader() 메서드 사용
#   csv 파일의 내용을 읽고 그 내용을 저장한 객체(데이터)를 반환

print('=== csv 모듈을 사용 ===')
import csv # csv 모듈 사용하기

with open('student.csv', 'rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # reader 객체 순회하여 각 줄을 출력
    for row in reader:
        print(row)
        

#? csv 모듈로 csv 파일 생성
# csv.writer 객체를 이용하여 csv 파일 작성
header = ['name', 'gender', 'age']
data = [
    ['이승아', '여', 30], # alt + shift + 방향키(위/아래)
    ['이도경', '여', 35], 
    ['김명진', '남', 32]
]

with open('C:\\python2-0110\\0110\\person.csv', 'wt', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # 한 줄 추가: writerow
    # 여러 줄 추가: writerows
    writer.writerow(header)
    writer.writerows(data)
    
print('csv 파일이 생성되었습니다 :)')