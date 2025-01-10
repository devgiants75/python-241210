### g_oop_example.py ###

# 학생 정보를 전달하는 student_info 함수
# : 이름, 학년, 반, 전화번호, 주소, 성적

def student_info(name, grade, class_number, phone, address, score):
    # 학생 정보를 print로 출력
    print(f'{name} / {grade} / {class_number} / {phone} / {address} / {score}')

student_info('이승아', 3, 2, '01011112222', '부산 연제구', 90)
# 이승아 / 3 / 2 / 01011112222 / 부산 연제구 / 90
student_info('이도경', 3, 7, '01033335555', '부산 부산진구', 100)
# 이도경 / 3 / 7 / 01033335555 / 부산 부산진구 / 100

#! 클래스를 활용한 학생 관리
# 학생 정보 전달 함수는 학생의 데이터를 저장하지 않음
# : 출력(소비)만 가능

class Student:
    def __init__(self, name, grade, class_number):
        self.name = name
        self.grade = grade
        self.class_number = class_number
        
    def print_info(self):
        print(f'Name: {self.name}, Grad: {self.grade}, ClassNumber: {self.class_number}')
            
student1 = Student('이승아', 3, 2)
student2 = Student('이도경', 1, 12)

student1.print_info() # 실제 데이터에서 기능 활용
student2.print_info()
# Name: 이승아, Grad: 3, ClassNumber: 2
# Name: 이도경, Grad: 1, ClassNumber: 12