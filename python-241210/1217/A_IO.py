# A_IO

# === 파이썬의 입력 ===
# cf) 출력: print()

# input(): 파이썬의 입력 함수, 사용자로부터 입력을 받음
# - 해당 함수는 사용자의 입력을 문자열로 인식하여 읽어옴
# - input('사용자에게 전달하고자 하는 메시지(출력)')
user_input = input('이름을 입력해주세요.')
print(f'사용자가 입력한 이름은 {user_input}입니다.')

# cf) 문자열을 정수, 실수로 바꿔주는 함수: int(), float()
height = float(input('키를 입력해주세요.'))
print(height)

str1 = input('첫 번째 숫자')
str2 = input('두 번째 숫자')
result = str1 + str2 # 문자열 끼리의 덧셈은 '문자열의 나열'
print(result) # 500300

num1 = int(str1)
num2 = int(str2)
sum = num1 + num2 # 숫자형 끼리의 덧셈은 '숫자의 계산'
print(sum) # 800

# 거스름돈 계산: 금액은 정수로 표현
# 사용자로부터 구매 금액 입력 purchase_amount
# 사용자로부터 지불 금액 입력 payment_amount
purchase_amount = int(input('구매 금액을 입력하세요.'))
payment_amount = int(input('지불 금액을 입력하세요.'))

# 거스름돈을 계산 change
change = payment_amount - purchase_amount

# >>> 출력: purchase_amount원의 물건 구매에 payment_amount원을 지불하여 change원의 거스름돈이 발생하였습니다.
print(f'{purchase_amount}원의 물건 구매에 {payment_amount}원을 지불하여 {change}원의 거스름돈이 발생')