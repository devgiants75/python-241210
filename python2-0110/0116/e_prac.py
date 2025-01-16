# e_prac.py

### 클래스 변수 / 클래스 메서드 / 정적 메서드 ###

#! 가방 공장
# 가방을 만들 때 마다, 현재 만들어진 가방이 몇 개인지 계산하는 Bag 클래스

class Bag:
    count = 0
    
    # 인스턴스 메서드이자 생성자 메서드
    def __init__(self):
        # 생성자 호출할 때마다 count가 1씩 증가
        # self 키워드를 대신해 클래스 내부에서 클래스명 사용 가능
        Bag.count += 1
        
    # 클래스 메서드
    @classmethod
    def sell(cls):
        cls.count -= 1 # 가방 판매 시 count가 1씩 감소
        
    # 클래스 메서드
    @classmethod
    def remain_bag(cls): # remain: 남아있는
        return cls.count # 남아있는 가방의 개수

# 클래스 메서드: 인스턴스화 이전에 호출 가능!
print('현재 가방: {}'.format(Bag.remain_bag())) # 현재 가방: 0
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}'.format(Bag.remain_bag())) # 현재 가방: 3
bag1.sell()
bag2.sell()
print('현재 가방: {}'.format(Bag.remain_bag())) # 현재 가방: 1

#! 전구 클래스
# 1. 전구가 생성될 때마다 전체 전구의 수를 추적 (클래스 메서드)
# 2. 전구가 판매 OR 폐기될 때 수를 증가/감소 (클래스 메서드)
# 3. 전구의 수명이 얼마나 남았는지 계산 (정적 메서드)

class LightBulb:
    total_count = 0
    
    def __init__(self):
        LightBulb.total_count += 1 
        
    @classmethod
    def sell_bulb(cls):
        if cls.total_count > 0:
            # 1개 이상 전구가 존재함 (판매 가능)
            cls.total_count -= 1
        else:
            # 전구의 재고가 없는 경우
            print('판매할 전구가 없습니다.')
            
    @classmethod
    def current_stock(cls):
        return cls.total_count
    
    @staticmethod
    def calculate_lifttime(hours):
        # 전구의 수명을 시간 단위로 받아, 평균적으로 몇 년 지속될지 계산
        
        # 1년: 약 8700시간
        # 10000시간(hours 매개변수값)을 사용할 수 있는 전구라면!
        # >> 1년 1300시간 사용 가능
        years = hours / (24 * 365)
        return years
    
# 클래스 사용
print('===전구 예제===')
print(f'초기 전구: {LightBulb.current_stock()}') # 초기 전구: 0

# 반복문을 사용하여 전구 5개를 생성
# : for in 반복문 + range() 함수
new_bulbs = [LightBulb() for _ in range(5)]

print(f'전구 생성 후: {LightBulb.current_stock()}') # 전구 생성 후: 5

LightBulb.sell_bulb()
LightBulb.sell_bulb()

print(f'전구 판매 후 {LightBulb.current_stock()}') # 전구 판매 후 3

lifetime = LightBulb.calculate_lifttime(10000)
print(f'전구의 수명: {lifetime:.2f}년') # 전구의 수명: 1.14년