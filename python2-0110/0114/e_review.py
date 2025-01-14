# e_review.py

#! Q) 다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성
# : title, author (인스턴스 변수 정의 - 직접 명시)

# 지시사항
# - 해당 객체에 매개변수값을 전달하는 set_info() 메서드를 구현
#   : 인스턴스 변수에 값을 할당
# - 책 제목과 책 저자 정보를 출력하는 print_info() 메서드를 구현
#   : f-string을 사용하여 변수의 값을 문자로 출력

# - book1과 book2 인스턴스(객체)를 생성
# - 생성된 인스턴스(객체)에 제목과 저자 정보를 저장

class Book:
    # 인스턴스 변수
    title = ''
    author = ''
    
    # 인스턴스 메서드
    def set_info(self, title, author):
        self.title = title
        self.author = author
        
    def print_info(self):
        print(f'Title: {self.title} / Author: {self.author}')
        
book1 = Book()
book2 = Book()

book1.set_info('어린왕자', '생택쥐페리')
book2.set_info('파이썬', '이승아')

book_list = [book1, book2]

for book in book_list:
    book.print_info()