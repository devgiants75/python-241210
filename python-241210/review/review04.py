# review04

### 학생 점수 분석 프로그램 ###

# 1. 요구사항
# : 다수의 학생 성적을 입력받아 성적 분석을 수행하는 프로그램 작성

# 2. 입력 형식
# 학생 이름과 점수를 콤마(,)로 구분
# 여러 명의 학생은 공백으로 구분

# 3. 출력
# 모든 학생의 평균 점수, 최고 점수 학생, 최저 점수 학생
# , 점수 80점 이상의 학생 리스트 출력

# 4. pandas 라이브러리 사용: 데이터를 DataFrame으로 변환 후 분석

import pandas as pd

input_data = input('학생 이름과 점수를 입력하세요. (예: 이승아,85 이도경,90 이지희,80 이지훈,75): ')

students = input_data.split(" ")

data = []
for student in students:
    name, score = student.split(",") # 이름과 점수를 쉼표로 분리
    data.append({"이름": name, "점수": int(score)}) # 딕셔너리 형태로 데이터 추가

# pandas DataFrame 생성
df = pd.DataFrame(data)

# 1. 평균 점수 계산
average_score = df["점수"].mean()
print(f'평균 점수: {average_score:.2f}')

# 2. 최고 점수와 해당 학생 이름
# df["점수"].max(): 최고 점수를 추출
# df["점수"] == df["점수"].max(): 열의 각 값이 최고 점수와 동일한지 비교
max_score_row = df[df["점수"] == df["점수"].max()]

# iloc[]: DataFrame에서 해당 행의 데이터만 반환
max_score_student = max_score_row.iloc[0]["이름"]
max_score = max_score_row.iloc[0]["점수"]

# 3. 최저 점수와 해당 학생 이름
min_score_row = df[df["점수"] == df["점수"].min()]
min_score_student = min_score_row.iloc[0]["이름"]
min_score = min_score_row.iloc[0]["점수"]

# 4. 점수 80점 이상인 학생 리스트
high_scores = df[df["점수"] >= 80]["이름"].tolist()

print(f'평균 점수: {average_score:.2f}')
print(f'최고 점수: {max_score_student} / {max_score}점')
print(f'최저 점수: {min_score_student} / {min_score}점')
print(f'80점 이상인 학생: {high_scores}')






