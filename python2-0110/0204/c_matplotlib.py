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
#1. figure
# : 하나의 그래프 창을 나타냄
#   , 여러 개의 subplot을 포함할 수 있는 정체 영역
#   (한 figure 안에 여러 개의 subplot이 포함될 수 있음)
# - 사용법
# : plt.figure() 함수를 사용하여 Figure 객체를 생성
# : plt.figure(figsize=너비, 높이)를 사용한 크기 조절 가능 (선택 옵션)