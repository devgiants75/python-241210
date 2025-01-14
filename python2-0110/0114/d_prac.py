# d_prac.py

# 클래스 생성 예제
# 자동차 클래스: Car
# - 각 자동차의 브랜드, 모델, 연료 타입, 색상 (인스턴스 변수)
# - 각 자동차가 수행할 수 있는 기본 동작
#       : 운전하기, 가속하기, 정지하기 (인스턴스 메서드)

class Car:
    # 인스턴스 변수 - 명시적으로 정의
    brand = ''
    model = ''
    fuel_type = ''
    color = ''
    
    # 인스턴스 메서드
    
    # 자동차가 기능하기 전 '생성'
    def set_details(self, brand, model, fuel_type, color):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.color = color
        
    def drive(self):
        print(f'{self.brand} {self.model} is driving')
        
    def accelerate(self):
        print(f'{self.fuel_type} 연료가 닳고 있습니다.')
        
    def stop(self):
        print('운행이 종료되었습니다.')
        
car1 = Car()
car2 = Car()

# 빈 값에 의해 출력 X: 오류 X (직접적인 인스턴스 변수 생성 - 객체 생성과 동시에 이루어짐)
print(car1.brand)
print(car2.model)

car1.set_details('Hyundai', 'Sonata', 'Gasoline', 'Black')
car2.set_details('Volvo', 'XC60', 'Diesel', 'White')

car1.drive()
car1.accelerate()
car1.stop()

car2.drive()
car2.accelerate()
car2.stop()