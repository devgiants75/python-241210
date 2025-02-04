# c_matplotlib.py

### 파이썬 데이터 시각화 라이브러리 - matplotlib ###

#! Matplotlib 라이브러리 사용 방법
# : cmd(명령 프롬프트), 터미널 설치
# > pip install matplotlib
# > pip list

#! matplotlib 라이브러리 불러오기
# : pyplot 모듈을 사용
# > plt 이름으로 축약하여 사용
import matplotlib.pyplot as plt

#? figure & subplot
# 1. figure
# : 하나의 그래프 창을 나타냄
#   , 여러 개의 subplot을 포함할 수 있는 정체 영역
#   (한 figure 안에 여러 개의 subplot이 포함될 수 있음)
# - 사용법
# : plt.figure() 함수를 사용하여 Figure 객체를 생성
# : plt.figure(figsize=너비, 높이)를 사용한 크기 조절 가능 (선택 옵션)
figure = plt.figure(figsize=(8, 6))

# 2. subplot
# : 실제로 그래프를 그리는 영역
# - 사용법
# : add_subplot() 함수를 사용하여 Figure 안에 Subplot을 추가
# >> 3가지의 파라미터를 필요로 함
#       nrows: 그리드의 행 수
#       ncols: 그리드의 열 수
#       index: 그래프를 그릴 위치(1부터 시작)

# 2행 2열의 subplot 생성
# axes1 = figure.add_subplot(2, 2, 1) # 2행 2열의 1번쨰 subplot # alt + shift + 방향키
# axes2 = figure.add_subplot(2, 2, 2) # 2행 2열의 2번쨰 subplot
# axes3 = figure.add_subplot(2, 2, 3) # 2행 2열의 3번쨰 subplot
# axes4 = figure.add_subplot(2, 2, 4) # 2행 2열의 4번쨰 subplot

axe1 = figure.add_subplot(3, 1, 1)
axe2 = figure.add_subplot(3, 1, 3)
# axe3 = figure.add_subplot(3, 1, 2)

# figure과 subplot 출력 
plt.show()

# 여러 개의 subplot을 동시에 생성
# : subplots() 함수를 사용
axes = plt.subplots(nrows=3, ncols=3)
plt.show()