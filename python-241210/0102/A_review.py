# A_review

### 정사각형과 원의 넓이를 계산하는 함수 모듈 ###

# 1. calculate_square 함수 (정사각형의 넓이 == 한 변의 길이 * 한 변의 길이)
# : 한 변의 길이를 인자로 받아 정사각형의 넓이를 반환
def calculate_square(side):
    return side * side

# 2. calculate_circle 함수 (원의 넓이 == 반지름 * 반지름 * pi)
# : 반지름을 인자로 받아 원의 넓이를 반환
# - 표준 라이브러리 math에 있는 pi 상수값을 사용
import math

def calculate_circle(radius):
    return radius * radius * math.pi 