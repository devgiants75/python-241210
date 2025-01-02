# C_external(외부의)

# 파이썬 외부 모듈 설치 및 사용
# : pip를 통해 외부 모듈을 설치

# == pip란 ==
# : 파이썬으로 작성된 패키지(라이브러리)를 관리하는 시스템
# : 외부 라이브러리를 설치하거나 삭제할 수 있음
# - 파이썬 설치 시 자동으로 설치

# == pip 환경변수 등록 ==
# : python 설치 경로 이동
# : 환경 변수 > 시스템 변수 > Path에 등록

# - C:\Users\user\AppData\Local\Programs\Python\Python312
# - C:\Users\user\AppData\Local\Programs\Python\Python312\Scripts

# == pip 기본 명령어 ==
# : cmd(명령 프롬프트)창에 입력

# 1. pip list
# : 현재 설치되어 있는 외부 모듈(라이브러리)의 리스트를 보여주는 명령어

# 2. pip install 패키지명
# : 해당 패키지 설치 명령어

# 3. pip uninstall 패키지명
# : 해당 패키지 삭제 명령어

# == 파이썬 외부 모듈(라이브러리) 사용 방법 ==
# : 일반 표준 모듈 사용법과 동일
# import 모듈명
#   , from 모듈명 import 항목명
#   , import 모듈명 as 별칭

### 파이썬 외부 모듈 - numpy ###
# : 수치 연산 라이브러리
# : 대규모 다차원 배열 & 행렬 연산(표)에 필요한 함수를 제공

# 설치 & 삭제
# cmd(명령 프롬프트)
#   > pip install numpy > pip list
#   > pip uninstall numpy > y (yes) > pip list

# 파이참에서 외부 모듈 & 패키지 설치: alt + shift + enter
import numpy as np

# 1. 1차원 배열 생성
# : np.array([요소1, 요소2, ...])
arr = np.array([1, 2, 3, 4, 5])
print(arr)

num_list = [1, 2, 3, 4, 5]
print(num_list) # [1, 2, 3, 4, 5]

# 2. 2차원 배열 생성
# np.array(([요소1, 요소2, ...], [요소1, 요소2, ...], [요소1, 요소2, ...], ...))
arr2 = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(arr2)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]] >> 3행 3열

# 3. 배열의 형태 확인
# 배열명.shape
print(arr2.shape) # (3, 3) >> 3행 3열

# 4. 배열 연산
# : 배열의 모든 요소에 대한 연산식 가능
arr3 = arr + 2 # arr == [1, 2, 3, 4, 5]
print(arr3) # [3 4 5 6 7]

# 5. 통계 함수 사용
# : 엑셀에서 사용하는 함수식 사용 가능 (평균값, 총합 등 계산)
print(np.mean(arr)) # 넘파이 배열의 평균값: np.mean(배열명) # 3.0
print(np.sum(arr2)) # 넘파이 배열의 총합: np.sum(배열명) # 45

### 파이썬 외부 모듈 - pandas ###
# : Python Data Analysis Library 약자
# : 파이썬에서 데이터 분석을 위해 사용되는 라이브러리
# - 구조화된 데이터(표 형태)를 다루기 위한 다양한 기능을 제공

# == 파이참을 사용한 외부 라이브러리 설치 ==
# 1. 왼쪽 상단 (햄버거 버튼) 메뉴바 > File > Settings (ctrl + alt + s)
# 2. 왼쪽 메뉴바: Project <프로젝트명>
#   : Python Interpreter 선택
#   : 현재 프로젝트에 설정된 Python 인터프리터와 설치된 패키지 목록 확인

# 3. 화면 왼쪽 상단의 + 버튼 클릭
#   : 패키지 설치 화면 확인
#   > 검색 바에서 패키지 검색
#   > 오른쪽 하단의 패키지 설치 버튼 클릭


