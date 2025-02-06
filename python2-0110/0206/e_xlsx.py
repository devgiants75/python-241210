# e_xlsx.py

# Pandas & Openpyxl 외부 라이브러리
# 1. Pandas
# : 데이터 분석을 위한 고수준의 자료 구조와 데이터 분석 도구를 제공

# 2. Openpyxl
# : Excel(.xlsx) 파일을 읽고 쓰기 위한 도구를 제공

#! 설치 명령어
# pip install pandas
# pip install openpyxl

#! pandas 라이브러리 활용
# : python 데이터 분석 라이브러리
# - 구조화된 데이터를 효율적으로 처리하고 분석

import pandas as pd

#! 1. Series
data = pd.Series([1, 3, 5, 7, 8]) # 1차원 레이블 배열
print(data)

data = pd.Series([2, 4, 6, 8, 10], index=['a', 'b', 'c', 'd', 'e'])
# >> 각각의 레이블을 별도로 지정
print(data)

#! 2. DataFrame
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [28, 34, 20, 35],
    'City': ['부산', '서울', '경기', '대전']
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['#1', '#2', '#3', '#4'])
print(df)

#! 데이터 프레임 활용
# : 데이터 프레임의 데이터 접근 
# 1) 단일 열 선택
print('=== DF 데이터 접근 ===')
print(df['Name'])
print(df['City'])
# print(df['Hobby']) - 존재하지 않는 키 접근 불가!

# 2) 여러 열 선택
print(df[['Name', 'City']]) # 대괄호 중첩 시: 이중 배열 - 2차원 배열

# 3) 행 필터링
# : 조건에 따른 행의 데이터 가져오기
result = df[df['Age'] >= 30]
print(result)

# 4) 데이터 조작
# : 새로운 열 추가
print(df)
df['Job'] = ['Develop', 'Employee', 'Singer', 'Engineer']
print(df)