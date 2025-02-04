# d_plot.py

### 선 그래프 (plot) ###
#! plot() 함수
# : 선 그래프를 그리기 위한 함수 (꺾은 선형 그래프)
# - x값, y값을 사용하여 2차원 선 그래프를 생성
# - plot(x, y): x와 y값에 각각의 데이터를 리스트 형태로 전달

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)

# x축의 값
x1 = [0, 1, 2, 3, 4]
x2 = [0, 1, 2, 3, 4]

# y축의 값
y1 = [4, 1, 3, 5, 2]
y2 = [0, 7, 5, 3, 1]

#! plot() 함수 커스터마이징
# 1) linestyle: 선 스타일 설정
# 실선(-, solid, 기본값) / 점선(., dotted) / 대시 (--, dashed)

# 2) linewidth: 선의 두께 설정
# 포인트(pt) 단위의 실수

# 3) color: 선의 색상 설정 - 영단어 키워드로 설정

# 4) marker: 각 데이터의 포인트에 대한 마커 설정
# o(원), ^(삼각형), s(사각형)

axes.plot(x1, y1, linestyle='dotted', linewidth='5.0', color='red')
axes.plot(x2, y2, linestyle='--', color='lightblue', marker='^')

# 그래프 제목 스타일링
# : matplotlib 라이브러리는 한글을 자동 처리하지 않음!
plt.title('Data Visualization - plot 선 그래프')
plt.xlabel('x축')
plt.ylabel('y축')

plt.show()