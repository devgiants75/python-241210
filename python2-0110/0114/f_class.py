# f_class.py

#! 생성자
# : 객체가 생성될 때 자동으로 실행되는 메서드
# >> 인스턴스 변수의 초기화를 담당하여 변수 접근의 오류를 방지

# cf) 인스턴스 메서드를 활용한 인스턴스 변수 초기화
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color
        
bananaCandy = Candy()
# print(bananaCandy.shape) # AttributeError: 'Candy' object has no attribute 'shape'
# >> 인스턴스 메서드를 호출하지 않으면 인스턴스 변수에 접근 불가!

bananaCandy.set_info('banana', 'yellow')
print(bananaCandy.shape)

#! 생성자를 이용한 인스턴스 생성
# 생성자
# : 인스턴스 생성 시 자동으로 호출!!

#? 생성자 형태
# __init__()
# : 파이썬에서는 생성자의 이름을 반드시 __init__으로 고정! (변경 X)
# : 생성자의 첫 번째 매개변수도 반드시 self 로 선언!

# cf) 파이썬에서의 __(언더바 2개) 메서드
# : 해당 메서드들은 미리! 기능과 역할이 부여된 메서드

class Candy2:
    def __init__(self, shape, color):
        # 생성자에 나열되는 매개변수는
        # : 클래스 호출로 인스턴스화 진행 시 인자값으로 전달
        # EX) Candy2('star', 'red')
        self.shape = shape
        self.color = color
        
# 생성자를 사용한 객체 생성
# : 생성자가 자동 호출: __init__ 생성자 호출을 하지 않아도 됨

# mangoCandy = Candy2() 
# TypeError: Candy2.__init__() missing 2 required positional arguments: 'shape' and 'color'
# >> 클래스 호출 시 반드시 생성자의 매개변수값을 전달해야 함!

appleCandy = Candy2('star', 'red')
print(appleCandy.shape, appleCandy.color) # star red

### 소멸자 ###
# : 인스턴스가 소멸될 때 자동으로 호출되는 메서드
# : 소멸 == 메모리에서 삭제
# : __del__()

# cf) init: initialize (시작하다, 생성하다)
#       del: delete (삭제하다, 소멸하다)

class Sample:
    # 반드시! 첫 번째 매개변수로 self 키워드 사용 
    def __del__(self):
        print('인스턴스가 소멸됩니다.')
   
# 변수명(소문자) / 클래스명(대문자)     
sample = Sample()

# 객체 삭제
# : del 키워드를 사용
# del 객체명
del sample

# print(sample) # NameError: name 'sample' is not defined. Did you mean: 'Sample'?

#? 파이썬 소멸자 사용 시 주의사항
# : __del__() 메서드는 객체가 메모리에서 제거될 때 호출
# : del 키워드를 통해 객체 삭제를 요구하여도 
#   , 소멸자 자체의 삭제 시점을 개발자가 명확하게 지정할 수 X
# >> 파이썬의 가비지 컬렉션의 동작 시점이 불분명

# 소멸자 사용을 권장하지 않음!