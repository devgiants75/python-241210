# F_module

# 파이썬 모듈(module)
# : 함수나 변수 또는 클래스 등을 모아 놓은 파일
# - 단위) .py 확장자를 가진 파이썬 파일
# : 재사용 가능한 코드 블럭을 만들어 다른 파이썬 프로그램에서 사용

# == 모듈의 필요성 ==
# 1. 코드의 재사용성
# : 한 번 작성하면 계속해서 재사용 가능
# - 개발 시간 단축 & 코드의 일관성 유지 용이

# 2. 코드의 구조화
# : 코드의 유지보수, 코드의 이해도 향상

# == 파이썬 모듈 사용 방법 ==
# import 키워드를 사용하여 '불러오기' 가능
# : .py(모듈 단위) 확장자를 생략하여 파일명만 작성

# Z_module.py 모듈을 불러오기
# : 불러온 모듈의 경우 사용하지 않으면 주석과 같이 희미하게 작성
# - 사용 시 검은색으로 표현
import Z_module

# import 한 모듈 사용 방법
# : 모듈명.함수명
# - 마침표의 기능: A.B - A 안의 B를 의미
print(Z_module.add(3, 5)) # 8
print(Z_module.subtract(13, 15)) # -2

# cf) 자동완성 단축키: ctrl + space

# from import 사용
# : from 모듈명 import 항목명
# : 특정 모듈에서 하나 이상의 특정 항목만 불러오기 가능
# - 항목을 사용할 때 모듈명을 접두어로 붙이지 않아도 사용 가능

# cf) 항목명 - 변수, 함수, 클래스명 등

from Z_module import greet, info, my_variable
# 여러 항목을 동시에 불러오는 경우 쉼표(,)를 사용하여 나열
print(greet('이승아')) # Hello, 이승아
print(info(169)) # I"m 169 tall

print(my_variable) # 새해 복 많이 받으세요

# import as 사용
# : 모듈의 이름이 길거나 다른 모듈과 충돌할 가능성이 있는 경우
# : 모듈에 대한 별칭(alias)을 지정하는 방법

import Z_module as zm
print(zm.add(10, 20))
print(zm.my_variable)

from Z_module import greet as hello
print(hello("이도경")) # Hello, 이도경