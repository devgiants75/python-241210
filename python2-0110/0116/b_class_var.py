# b_class_var.py

### 클래스 변수 ###

# 1. 클래스 변수 정의
# : 클래스 내부에서 정의되지만 메서드 외부에서 선언되는 변수
# : 해당 클래스의 모든 인스턴스에서 '공유되는 값'을 저장
# >> 메모리 공간의 낭비를 방지
# EX) 한국 사람 클래스 - 소속 국가, 국기 등 (한국 사람이면 모두 같은 값)

# cf) 인스턴스 변수
# : 인스턴스 마다 '서로 다른 값'을 가지는 경우에 인스턴스 변수를 사용
# >> 모든 인스턴스 변수는 self 키워드를 붙여 사용
# EX) 한국 사람 클래스 - 이름, 나이, 주소, 주민등록번호 등 (사람마다 다른 값)

class Korean:
    # 클래스 변수
    country = '한국'
    
    def __init__(self, name, age, address):
        # 인스턴스 변수는 반드시 self 키워드 작성
        self.name = name
        self.age = age
        self.address = address
        
person1 = Korean('이승아', 30, '부산시')
person2 = Korean('이도경', 25, '대전시')

# 인스턴스 변수에 접근
# : 인스턴스명.변수명
# >> 해당 인스턴스를 통해서만 접근 가능!
        
print(person1.name)
print(person1.address)
print(person2.name)

# 클래스 변수에 접근
# : 인스턴스가 생성되지 않아도 접근 가능!
# : 클래스명.변수명 OR 인스턴스명.변수명 모두 가능
# >> 클래스명으로의 접근을 권장

print(Korean.country)
print(person2.country)

# 값의 변경(인스턴스 VS 클래스)
person2.name = '이현아'
print(person1.name) # 이승아
print(person2.name) # 이현아 - 값을 수정한 인스턴스만 영향을 받음

Korean.country = '대한민국'
print(person1.country)
print(person2.country)
print(Korean.country)

person1.country = 'Korea'
print(person1.country) # 클래스 변수를 클래스를 통해서만 접근해야하는 이유!
print(person2.country)
print(Korean.country)

# 인스턴스 변수 - 고유한 값 저장, 인스턴스를 통해서만 접근!
# 클래스 변수 - 공유되는 값 저장, 인스턴스 or 클래스를 통해서 접근!