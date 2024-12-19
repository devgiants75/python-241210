# C_practice

# 리스트 & 튜플 예제
# === 식료품점에서 구매할 물품과 각각의 가격을 정리 ===
# : 각 항목의 가격을 변수에 저장하고
# : 총 구매 금액을 계산
groceries = [('사과', 5000), ('우유', 3000), ('빵', 1500)]

# 각 항목의 가격을 계산
apple_price = groceries[0][1]
milk_price = groceries[1][1]
bread_price = groceries[2][1]

# 총 구매 금액을 계산
# 오늘의 가계부: 식료품 - 총 금액 {total_price}원
total_price = apple_price + milk_price + bread_price

# 오늘의 가계부: 식료품 - 총 금액 9500원
print(f'오늘의 가계부: 식료품 - 총 금액 {total_price}원')