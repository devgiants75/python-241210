# z_prac.py

### 데이터 시각화 예제 ###

#! 차트 생성
# : 시간의 경과에 따른 데이터 변화를 보여주는 예제
# : 일주일 간의 온도 변화를 나타내는 차트

import matplotlib.pyplot as plt

#! 활용 데이터
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 18, 19, 20, 16, 14]

cities = ['NY', 'LA', 'CCG']
rainfall = [1200, 900, 850]

# figure과 subplot 동시 생성
# : figure = plt.figure()
# : axe = figure.add_subplot()

# 1행 2열의 subplot 구성: 각각의 축 ax1과 ax2를 반환
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

#? 라인 차트 생성
# : ax1(첫 번째 서브플룻) - plot() 라인 차트
ax1.plot(weeks, temperature)
# subplot (서브플룻)의 이름표 설정
# : set_ 키워드를 각각의 이름표 앞에 작성
ax1.set_xlabel('Day')
ax1.set_ylabel('Temperature (C)')
ax1.set_title('Daily Temperatures in February')

#? 막대 그래프 생성
# ax2(두 번째 서블플룻) - bar() 막대 차트
ax2.bar(cities, rainfall)
ax2.set_xlabel('City')
ax2.set_ylabel('Annual Rainfall (mm)')
ax2.set_title('Annual Rainfall by City')

# 그래프 표시
plt.tight_layout() # subplot간의 충돌 방지
plt.show()