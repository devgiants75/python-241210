# C_practice

# 700원짜리 음료수를 뽑을 수 있는 자판기 프로그램 구현
# - 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지
#   , 잔돈은 얼마인지 모든 경우의 수를 출력

# == 함수 정의 == #
# 반환값 X: 데이터 출력(print())
# 함수 이름: vending_machine
# 매개변수: money(정수)

# ex) 3000원을 넣었을 때: 4잔의 음료수, 잔돈 200원

def vending_machine(money):
    # 자판기에 돈을 넣으면, 음료와 잔돈을 print()로 반환

    # 음료수 가격
    drink_price = 700

    # 음료수 개수 & 잔돈 계산
    # 계산 결과의 몫 - //
    # 계산 결과의 나머지 - %

    # 돈을 음료 가격으로 나눈 몫
    num_drink = money // drink_price

    # 돈을 음료 가격으로 나눈 나머지
    change = money % drink_price

    # 출력
    print(f'{money}원을 넣었을 때: {num_drink}잔의 음료, 잔돈 {change}원')

vending_machine(3000) # 3000원을 넣었을 때: 4잔의 음료, 잔돈 200원
vending_machine(5000) # 5000원을 넣었을 때: 7잔의 음료, 잔돈 100원
vending_machine(5600) # 5600원을 넣었을 때: 8잔의 음료, 잔돈 0원