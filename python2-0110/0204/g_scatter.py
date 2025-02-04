# g_scatter.py


### 선점도 (scatter) ###
#! scatter() 함수
# : 2차원 데이터에 대한 선점도를 그리는데 사용
# - 데이터 포인트 간의 관계를 시각화하는데 사용

import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)

# 데이터의 위치 지정
x = [1, 2, 3, 4, 5, 6]
y = [6, 4, 1, 2, 7, 5]

#! 선점도 커스터마이징
# : 해당 데이터에 대한 크기, 색상 지정 - 옵션 지정
area = [50, 100, 150, 200, 170, 30]
color = ['red', 'green', 'blue', 'orange', 'pink', 'aqua']

# s옵션으로 크기값, c옵션으로 색상을 지정
axes.scatter(x, y, s=area, c=color)
plt.show()