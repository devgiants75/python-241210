# b_class.py

### 클래스의 구성 ###

# 클래스
# : 현실 세계의 개념이나 사물을 코드로 모델링하기 위해 사용되는 프로그래밍의 구조적 단위

# EX) 사람
# 사람이 가지는 값: 이름, 나이, 연락처, 주소, ...
# 사람이 할 수 있는 기능:잔다, 먹는다, 공부한다, 걷는다, ...

#! 1. 클래스의 구성: 변수 & 함수
# 변수 - 값(객체의 상태를 저장)
# 함수(메서드) - 기능(객체가 수행할 수 있는 동작을 정의)

# cf) 클래스 내부의 함수가 메서드(method, 메소드)라고 불림

#? 클래스 내에 정의된 변수
# : 클래스 변수 & 인스턴스 변수

#? 클래스를 구성하는 함수 - 메서드(method)
# : 클래스 메서드 & 정적 메서드 & 인스턴스 메서드

#! 2. 인스턴스 변수 & 메서드

#? 1) 인스턴스 변수
# : 클래스를 기반으로 만들어지는 모든 인스턴스(객체)들이 "개별적으로" 가지는 데이터
# - 클래스 내에 정의되지만, 각 인스턴스에서 독립적으로 값을 가짐
# - 각 객체의 상태 저장
#       : 인스턴스 변수의 형태(self.variable_name)

#? 2) 인스턴스 메서드
# : 클래스 내에 정의된 함수(def), 클래스의 객체가 수행할 수 있는 동작
# - 주로 인스턴스 변수(독립적인 값)를 사용하는 메서드
# - 첫 번째 인자(매개변수)로 self를 받아야 함
#       self: 메서드를 호출하는 객체 자신을 참조

#? Person 클래스 정의
class Person:
    # 인스턴스 메서드 - 첫 번째 매개변수(인자) self
    def who_am_i(self, name, tel, address):
        # 인자값을 매개변수로 받아 객체 자신에게 전달
        self.name = name
        self.tel = tel
        self.address = address
        
        # self.a = a
        # self.a에서 a는 인스턴스 변수를 의미
        # 우항의 a는 매개변수 a를 의미
        # >> 인스턴스 메서드(who_am_i()) 호출 시 전달된 인자값이 인스턴스의 a에 전달됨
        
#? 객체(인스턴스) 생성
seungah = Person()

# 객체(인스턴스)를 사용하여 클래스 내에 정의된 변수와 메서드 접근 방법
# : .(마침표)를 사용
# - 객체명.변수명 / 객체명.메서드명()

# print(seungah.name) # AttributeError: 'Person' object has no attribute 'name'
seungah.who_am_i('이승아', '010-1111-2222', '부산시')
print(seungah.name) # 이승아 

# 실행 단축키: ctrl + f5

dokyung = Person()
dokyung.who_am_i('이도경', '010-3333-5555', '대전시')
print(dokyung.name)
print(dokyung.tel) # alt + shift + 방향키(위/아래): 줄 복사
print(dokyung.address)

# 인스턴스 메서드는 반드시 첫 번째 인자로 self 값을 가져야 함.
# : self는 66번 째 줄의 해당 메서드를 호출하는 객체 그 자체
# >> 인자로 전달되는 name, tel, address의 매개변수값은
# >> dokyung.name = '이도경'
# >> dokyung.tel = '010-3333-5555'
# >> dokyung.address = '대전시' 와 동일

# : 값이 할당되는 시점에 인스턴스 변수 생성