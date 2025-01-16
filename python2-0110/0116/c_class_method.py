# c_class_method.py

### 클래스 메서드 ###

#! 1. 클래스 메서드 정의
# : 클래스에 속한 메서드
# : @classmethod 데코레이터를 사용하여 정의된 메서드

# cf) 데코레이터는 코드로 표현하는 주석
#   >> @classmethod는 해당 메서드가 인스턴스 메서드가 아닌 클래스 메서드 임을 명시

class MyClass:
    class_var = '클래스 변수'
    
    @classmethod
    def class_method(cls):
        return cls.class_var
    
#! 2. 클래스 메서드 특징
# - 첫 번째 매개변수로 클래스 객체를 받음. (cls 키워드 사용)
# - 인스턴스 객체 없이도 호출 가능
#       : 클래스명으로 호출(클래스명.클래스변수())
#       : 인스턴스 & 클래스 호출이 모두 가능

class Korean:
    # 클래스 변수
    country = '한국'
    
    @classmethod
    def trip(cls, country):
        if cls.country == country: # cls: 클래스 객체, country: 매개변수
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')
            
# 국내 여행
Korean.trip('한국')
Korean.trip('미국')

# 클래스 변수 & 클래스 메서드 호출 시 유의사항!
# : 파이썬의 경우 인스턴스를 통해서도 클래스의 요소에 접근 가능!
# >> 클래스로만 호출하여 값의 할당, 사용을 권장!!