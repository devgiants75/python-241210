# review03

### 쇼핑몰 할인 계산기 ###

# 요구사항 #
# 1. 사용자가 구매한 상품의 가격과 수량을 입력받아
#   최종 결제 금액을 계산

# 2. 입력 형식
#   - 각 상품의 가격과 수량은 쉼표로 구분된 문자열로 입력
#       5000,2
#       3000,4

# 3. 할인 조건
#   - 상품 총 금액이 10만원 이상: 10% 할인
#   - 상품 총 금액이 20만원 이상: 20% 할인

# 4. 출력 형식
#   - 총 결제 금액, 할인 금액, 할인 적용 후 금액 출력

### 풀이 ###

# 사용자로부터 상품 가격과 수량 입력 받기
input_data = input("상품 가격과 수량을 입력하세요 (예: 5000,2 3000,4 1500,6): ")

# 입력 데이터를 공백으로 구분하여 리스트로 변환
items = input_data.split(" ")

# 총 상품 금액 계산
total_amount = 0  # 총 금액 초기화
for item in items:
    price, quantity = map(int, item.split(","))  # 가격과 수량을 쉼표로 분리
    total_amount += price * quantity  # 각 상품의 총 금액을 더하기

# 할인 금액 계산
discount = 0
if total_amount >= 200000:  # 총 금액이 20만 원 이상일 경우
    discount = total_amount * 0.2
elif total_amount >= 100000:  # 총 금액이 10만 원 이상일 경우
    discount = total_amount * 0.1

# 최종 결제 금액 계산
final_amount = total_amount - discount

# 결과 출력
print(f"총 상품 금액: {total_amount}원")
print(f"할인 금액: {int(discount)}원")
print(f"최종 결제 금액: {int(final_amount)}원")