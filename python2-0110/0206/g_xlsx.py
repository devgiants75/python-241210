# g_xlsx.py

# g_excel.xlsx 파일 생성


### pandas를 사용한 엑셀 불러오기 실습 ###

import pandas as pd

# 1. 엑셀 파일 경로 지정
file_path = 'g_excel.xlsx'

# 2. pandas 라이브러리의 read_excel함수 사용하여
#    DataFrame 형태로 불러오기
df = pd.read_excel(file_path)

# 3. 상위 5개의 행을 출력하여 조회
print('상위 5개 행 조회')
print(df.head())

# 4. 해당 DataFrame의 정보를 조회
print('---데이터프레임 정보---')
df.info()

# 5. 수치형 데이터에 대한 기초 통계 정보를 조회
print('---기초 통계 정보---')
print(df.describe())