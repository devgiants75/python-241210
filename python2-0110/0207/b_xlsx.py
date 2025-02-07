# b_xlsx.py

#! openpyxl의 엑셀 불러오기
# : 파일 그대로를 가져와서 저장

#! pandas의 엑셀 불러오기
# : DataFrame 형태로 변환

# >> 각각의 데이터 구조를 사용 가능 (파악하기 용이)

### 셀 내용 수정 및 삽입 ###
import pandas as pd
df = pd.read_excel('friend.xlsx')

# 두 번째 행의 City 열 값을 변경
# : loc 기능을 사용 (locate - 위치)
# > 데이터 행 부터 인덱스 번호 시작
df.loc[1, 'City'] = '광주'

df.loc[8] = ['장지민', '양산']

# 반복문을 사용하여 셀 정보에 접근
# : 모든 행의 'Name'열에 접근
print('--- 모든 행 이름 출력 ---')
for index, row in df.iterrows():
    print(row['Name']) 

# 특정 열 추가
df['Age'] = [1, 2, 3, 4, 5, 6, 7]

# 특정 열 삭제
# : drop('삭제하고자하는 열의 이름')
df.drop('Age', axis=1, inplace=True)
# >> axis=1 (행), axis=0 (열)
# >> inplace=True: 원본 데이터 수정

df.to_excel('friend.xlsx', index=False)