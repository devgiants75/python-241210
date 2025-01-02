# B_result

# A_review.py 모듈을 사용

# 1. import
# : 변의 길이가 10인 정사각형의 넓이를 계산하고 출력
# : 반지름이 5인 원의 넓이를 계산하고 출력

import A_review
# import 모듈명(파일명)
# : .py 모듈 확장자는 생략

# 모듈 내의 기능(함수, 변수 등) 사용
# 모듈명.기능명
result1 = A_review.calculate_square(10)
result2 = A_review.calculate_circle(5)
print(result1) # 100
print(result2) # 78.54

# 2. from import
# : A_review.py 모듈에서 calculate_square 함수만 import하여
# : 변의 길이가 7인 정사각형의 넓이를 계산하고 출력

from A_review import calculate_square
# from 모듈명(파일명) import 항목명(변수, 함수, 클래스)
result = calculate_square(7)
print(result) # 49

# 3. import as
# : A_review.py 모듈을 a라는 별칭(alias)으로 import하여
# : 반지름이 10인 원의 넓이를 계산하고 출력

import A_review as a
# import 모듈명(파일명) as 별칭

result = a.calculate_circle(10)
print(result) # 314.1