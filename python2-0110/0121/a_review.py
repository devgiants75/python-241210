# a_review.py

### 파이썬 클래스 복습 문제 ###
# [ 분식점 가게 매출 기능 구현 ]

# 객체 지향 프로그래밍
# 1. Shop 클래스
# : 전체 매출액을 저장 - total 클래스 변수
# : 메뉴 리스트를 딕셔너리로 저장(메뉴명-가격) - menu_list 클래스 변수
class Shop:
    # 클래스 변수
    total = 0
    menu_list = [{'떡볶이': 3000}, {'어묵': 700}, {'튀김': 500}, {'김밥': 2000}]
    
    # 클래스 메서드
    @classmethod
    def sales(cls, menu, amount):
        # 매개변수로 메뉴와 수량을 가져와 메뉴가 가게의 메뉴인지 확인
        # >> 메뉴가 존재할 경우: 메뉴 가격 * 수량 == 매출
        # >> 메뉴가 존재하지 X 경우: 메시지 출력
        for item in cls.menu_list:
            if menu in item:
                cls.total += item[menu] * amount # 딕셔너리명[키]: value값 반환
                return
            
        print(f'{menu}는 저희 가게 메뉴에 없습니다.')
        
# 매출이 생기면 메뉴와 판매량을 작성
Shop.sales('떡볶이', 1) # 3000
Shop.sales('튀김', 3) # 1500
Shop.sales('김밥', 2) # 4000
Shop.sales('국수', 1) # 국수는 저희 가게 메뉴에 없습니다.

# 총 매출
print(f'총 매출은 {Shop.total}원 입니다.') # 총 매출은 8500원 입니다.

# >> 클래스 변수, 클래스 메서드는 '클래스.'를 통해 호출하고 사용!

### 파이썬 클래스 상속 복습 문제 ###

# 차량 관리 시스템
# Vehicle (운송수단) 클래스 - 부모 클래스
# Car (자동차) 클래스 - 자식 클래스

class Vehicle:
    def __init__(self, make, model, year):
        # [인스턴스 변수]
        self.make = make # 제조 회사
        self.model = model # 모델명
        self.year = year # 제조 년도
        
    def description(self):
        return f'{self.year} {self.make} {self.model}'
    
    def drive(self):
        print(f'{self.description()} is now driving')
        
class Car(Vehicle):
    def __init__(self, make, model, year, trunk_size):
        # 자식 생성자
        # : 반드시! 부모 생성자의 호출이 이루어져야 함!
        # : super()
        super().__init__(make, model, year)
        self.trunk_size = trunk_size # Car 클래스 만의 인스턴스 변수
        
    def open_trunk(self):
        # 부모의 메서드를 상속받아 description 호출이 가능!
        print(f'{self.description()} / Trunk size: {self.trunk_size}')
        
vehicle = Vehicle('Hyundai', 'sonata', 2024)
print(vehicle.description()) # 2024 Hyundai sonata
vehicle.drive() # 2024 Hyundai sonata is now driving

car = Car('Kia', 'k7', 2023, 450)
print(car.description()) # 부모 클래스의 메서드: 2023 Kia k7
car.open_trunk() # 2023 Kia k7 / Trunk size: 450