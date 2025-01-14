# 생성자 & 소멸자 예제 #

class Service:
    def __init__(self, service):
        self.service = service
        print(f'{self.service} 서비스가 시작되었습니다.')
        
    def __del__(self):
        print(f'{self.service} 서비스가 종료되었습니다.')
        
service = Service('길 안내') 
# 길 안내 서비스가 시작되었습니다.
# 길 안내 서비스가 종료되었습니다. - 인스턴스 삭제 이전에도 소멸자가 실행

# 객체 사용 후 재사용 이전까지는 자동으로 메모리에서 삭제
# : 사용 시점이 개발자의 의도와 다름

del service