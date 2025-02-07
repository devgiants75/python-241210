# c_practice.py

### pandas, openpyxl을 활용한 엑셀 관리 ###
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side

#! 1. pandas > 엑셀 파일 불러오기
df = pd.read_excel('sales_data.xlsx')

#! 2. 셀의 데이터 출력
# : pandas 라이브러리는 해당 엑셀의 데이터를 구조화하여 가져옴
print(df) 

#! 3. 셀의 정보 출력 & 기초 통계 데이터 출력
df.info()
print(df.describe())

#! 4. 데이터의 상위 5개 행 출력
print(df.head())

#! 5. 각 제품별 총 판매량을 계산
# : 데이터프레임.groupby('열이름')['그룹화할 열 이름']
# >> 동일한 '열이름'별로 '그룹화 할 열'의 데이터를 그룹화
# .sum(): 그룹화 되어 있는 데이터에 대한 계산식
# .reset_index(): 전체 그룹화 된 데이터들의 인덱스 번호 초기화
total_sales = df.groupby('Product')['Quantity'].sum().reset_index()
print(f'각 제품별 총 판매량: ${total_sales}')

#! 6. 각 제품별 총 매출 계산
# : Quantity * Price
df['Total Revenue'] = df['Quantity'] * df['Price']

# 각가의 열에 대한 계산에서 동일한 제품명 끼리 묶어서 저장
# : 그룹화하여 집계함수를 사용
total_revenue = df.groupby('Product')['Total Revenue'].sum().reset_index()

print(f'각 제품별 총 매출: ${total_revenue}')