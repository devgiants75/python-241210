# g_상속.py

### 상속 예시 ###
# : 학생-사람 클래스의 관계를 상속으로 구현

# 부모 클래스
class Person:
    # 인스턴스 변수 name
    # : 생성자를 통해 초기화
    def __init__(self, name):
        self.name = name
        
    def eat(self, food):
        print(self.name + '이(가) ' + food + '를 먹습니다.')
        
# 자식 클래스
class Student(Person):
    # name = '' (인스턴스 변수 생성 방법 1)
    
    def __init__(self, name, school):
        # self.name (인스턴스 변수 생성 방법 2)
        
        # super() 함수
        # : 자식 클래스에서 부모 클래스의 속성이나 메서드에 접근
        # >> 인자로 받은 name의 값을 super()를 통해 부모에게 전달
        super().__init__(name)
        # : 부모 클래스의 생성자를 호출
        self.school = school
        
    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부합니다.')
        
#? 객체 생성
seungah = Student('이승아', '코리아IT학교')
seungah.eat('아이스크림') # 이승아이(가) 아이스크림를 먹습니다.
seungah.study() # 이승아은(는) 코리아IT학교에서 공부합니다.

dokyung = Person('이도경')
dokyung.eat('초콜릿') # 이도경이(가) 초콜릿를 먹습니다.
# dokyung.study() - AttributeError: 'Person' object has no attribute 'study'

#? cf) 자식 클래스의 생성자
#       : 자식 클래스 생성자 호출 시 super()함수를 사용해 부모 클래스의 생성자도 반드시 호출

# isinstance(객체, 클래스) 함수
# : 객체가 클래스의 인스턴스인지 확인하는 함수
# >> 결괏값을 불리언(Boolean) 값으로 반환

print(isinstance(seungah, Student)) # True
print(isinstance(seungah, Person)) # True

print(isinstance(dokyung, Student)) # False
print(isinstance(dokyung, Person)) # True