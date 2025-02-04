# f_bar.py

### 막대 그래프 (bar) ###
#! bar() 함수
# : 수직 및 수평 막대 그래프를 그리는 데 사용
# - 주로 범주형 데이터의 각 항목에 대한 값을 비교할 때 사용

import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(121) # 1행 2열의 1번째
axes2 = figure.add_subplot(122) # 1행 2열의 2번째

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [5, 6, 7, 2, 8, 5, 3]

#! 막대 그래프 커스터마이징
# color: 막대의 색상 설정 - 영단어 키워드 사용
# edgecolr: 막대 테두리 색상 설정
# barh(): 수평 막대 그래프 (h: horizon 수평선)

axes1.bar(x, y)
axes2.barh(x, y, color='skyblue', edgecolor='red')

plt.title('weekday chart')
plt.show()