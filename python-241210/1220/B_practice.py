# B_practice

# 조건문 정리 #
# 1. if문: 조건이 참일 때만 코드 실행
# 2. (if) else문: 조건이 거짓일 때만 코드 실행
# 3. 중첩 if-else문: 조건문 내부의 조건문
# 4. elif문: 여러 조건을 순차적으로 확인
# 5. 삼항 연산자: 조건문을 간결하게 표현

# 1. 사용자로부터 입력 받은 숫자가 짝수인지 홀수인지 판별하는 프로그램
# num 변수에 사용자로부터 숫자를 입력받기 : input
# # 입력받은 숫자가 짝수인지 홀수인지 판별 : if-else

num = int(input('숫자를 입력해주세요.'))

if num % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# 2. 중첩 조건문을 이용한 성적 분류 프로그램

score = int(input('성적을 입력하세요.(0 ~ 100): '))

# 성적이 유효한 범위인지 확인

if score < 0 or score > 100:
    print('유효하지 않은 점수입니다.')
else:
    # 유효한 숫자만 입력 (0 ~ 100)
    # 성적에 따라 등급 분류: 90점 이상(A), 80점 이상(B), 70점(C), 그외에는 F
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'F'
    print(f'학생의 등급은 {grade}입니다.')

# 딕셔너리를 사용한 항목 관리

items = {'사과': 2000, '바나나': 1500, '체리': 900}

item_name = '사과'

# 딕셔너리 값 추출: 딕셔너리명[키명]
if item_name in items:
    print(f'{item_name}의 가격: {items[item_name]}')
else:
    print('해당 물품이 없습니다.')