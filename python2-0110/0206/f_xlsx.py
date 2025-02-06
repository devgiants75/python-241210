# f_xlsx.py

### 엑셀 파일 활용 with. pandas ###

import pandas as pd

#! 1. 엑셀 파일 불러오기
# f_excel.xlsx

file_path = 'f_excel.xlsx' # 파일 경로 지정

df = pd.read_excel(file_path) # 엑셀 파일 불러오기
print(df)

#! 2. 데이터 조회하기
#? 상위 데이터 조회
print(df.head()) # 상위 5개 행을 조회

#? 데이터 프레임 정보 조회
df.info() # DF의 구조(컬럼), 각 컬럼의 데이터 타입 분석 조회

#? 기초 통계 정보 조회
print(df.describe()) # 수치형(숫자) 컬럼들에 대한 기본 통계 정보
# >> 평균, 표준편차, 최소값, 최대값 등을 조회