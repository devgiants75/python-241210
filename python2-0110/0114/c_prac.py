# c_prac.py

# 클래스 예제 #

# 사용자로부터 온전한 수식을 입력받고, 입력된 수식의 결과를 출력하는 Calculator 클래스
# 파이썬 내장 함수: input(), eval()

# cf) input(): 사용자로부터 터미널에서 입력을 받는 함수
#       eval(): 문자열로 된 수식 자체를 계산할 수 있는 함수

class Calculator:
    
    def input_expr(self):
        # 수식을 입력받아 인스턴스 변수인 expr에 저장
        expr = input('수식을 입력하세요 >>')
        self.expr = expr # 우항의 expr은 15번째 줄의 입력값
        
    def calculate(self):
        # 인스턴스 변수에 저장되어 있는 문자열을 활용
        return eval(self.expr)
    
# Calculator 클래스를 기반으로 calc 인스턴스 생성
calc = Calculator()

calc.input_expr() # 인스턴스 변수에 수식 저장
result = calc.calculate() # 인스턴스 변수에 저장된 수식을 계산하여 결과 반환
print(f'수식 결과는 {result}입니다.')

# cf) 터미널 실행 환경 종료 - 터미널에 마우스 클릭 (활성화) ctrl + c