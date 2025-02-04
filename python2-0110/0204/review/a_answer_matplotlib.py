# 문제 1: plot() 함수 사용하기 - 시간에 따른 판매량 변화 선 그래프
import matplotlib.pyplot as plt

# 시간과 판매량 데이터
time = [1, 2, 3, 4, 5]
sales = [3, 5, 2, 7, 9]

# 선 그래프 그리기
plt.plot(time, sales, color='red')
plt.xlabel('시간')
plt.ylabel('판매량')
plt.title('시간 대비 판매량 변화')
plt.show()

# 문제 2: bar() 함수 사용하기 - 제품별 판매량 바 차트
import matplotlib.pyplot as plt

# 제품과 판매량 데이터
products = ['A', 'B', 'C', 'D']
sales = [10, 15, 7, 10]

# 바 차트 그리기
colors = ['blue', 'green', 'red', 'cyan']
plt.bar(products, sales, color=colors)
plt.xlabel('제품')
plt.ylabel('판매량')
plt.title('제품별 판매량')
plt.show()

# 문제 3: scatter() 함수 사용하기 - 변수 X와 Y의 관계 산점도
import matplotlib.pyplot as plt

# 변수 X와 Y 데이터
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# 산점도 그리기
plt.scatter(x, y, color='blue', s=50) # s는 마커의 크기
plt.xlabel('X 변수')
plt.ylabel('Y 변수')
plt.title('X와 Y의 관계')
plt.show()
