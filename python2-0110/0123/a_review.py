# a_review.py

# 다음 지시사항을 읽고 Hybrid 클래스를 구현

# 지시사항
# : 다음과 같은 슈퍼 클래스 Car를 가지고 있는 서브 클래스 Hybrid를 구현

# 1. 슈퍼 클래스 Car 구현
# Car 클래스는 최대 주유량(max_oil)을 클래스 변수로 가지며, 이 값은 50으로 설정

# __init__ 메서드를 통해 초기 주유량(oil)을 설정

# add_oil 메서드를 통해 주유를 추가할 수 있으며
# , 주유량이 0 이하이거나 최대 주유량을 초과하는 경우의 처리가 필요

# car_info 메서드를 통해 현재 주유 상태를 출력

class Car:
    max_oil = 50
    
    def __init__(self, oil):
        self.oil = oil # self.oil: 인스턴스 변수
        
    def add_oil(self, oil):
        if oil <= 0:
            return # 메서드 종료
        
        self.oil += oil
        
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil # 주유 후 최대 주유량 초과 상태이면 현재 주유량을 최대 주유량으로 설정
            
    def car_info(self):
        print(f'현재 주유상태: {self.oil}')

# 2. 서브 클래스 Hybrid 구현
# Hybrid 클래스는 Car 클래스를 상속

# 최대 배터리 충전량(max_battery)을 클래스 변수로 가지며, 이 값은 30으로 설정

# __init__ 메서드를 통해 초기 주유량(oil)과 배터리 충전량(battery)을 설정

# charge 메서드를 통해 배터리를 충전할 수 있으며
# , 충전량이 0 이하이거나 최대 충전량을 초과하는 경우의 처리가 필요

# hybrid_info 메서드를 통해 현재 주유량과 충전량을 모두 확인
class Hybrid(Car):
    max_bettery = 30
    
    def __init__(self, oil, battery):
        super().__init__(oil)
        self.battery = battery
        
    def charge(self, battery):
        if battery <= 0:
            return # 0 이하로 충전하는 것을 방지
        
        self.battery = battery
        
        if self.battery > Hybrid.max_bettery:
            self.battery = Hybrid.max_bettery
            
    def hybrid_info(self):
        self.car_info() # 슈퍼 클래스의 정보를 출력
        print(f'현재 충전 상태: {self.battery}')

#! 동작 확인
# Hybrid 인스턴스를 생성하고, 주유와 충전을 진행한 후
# , 현재 상태를 출력하여 모든 기능이 올바르게 동작하는지 확인
sonata = Hybrid(0, 0)
sonata.add_oil(55)
sonata.car_info()
sonata.charge(20)
sonata.hybrid_info()