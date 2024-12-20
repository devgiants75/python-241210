# E_practice

# 반복문 예시 1 #

#! 1부터 10까지 합을 구하는 프로그램 작성
# >> for 반복문과 산술 연산자 사용

# 합계를 저장할 변수 total을 0으로 초기화
total = 0

# for 반복을 사용하여 1부터 10까지 합산
# : += 연산자 활용

for i in range(1, 11):
    total += i

print(total) # 55

# 반복문 예시 2 #
# 사용자로부터 양의 정수 입력
num_of_fruits = int(input('입력할 과일의 개수를 입력하세요: '))

# basket 빈 리스트 생성
basket = []

# range(n)함수: n번 반복 (0 ~ n-1)

for i in range(num_of_fruits):
    fruit = input('과일 이름을 입력하세요.')
    basket.append(fruit)
print('과일 바구니: ', basket)