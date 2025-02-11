# answer.py

import sys # 프로그램 종료 시 사용되는 sys 모듈

#! Person 클래스 
# : 각 개인의 정보를 저장할 클래스
# : 이름(name), 전화번호(phone), 주소(address)

class Person:
    # 생성자(인스턴스 메서드의 일종)
    # : 객체 생성 시 호출, 초기값 설정
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        
    # 인스턴스 메서드
    # : 저장된 개인 정보를 출력
    def info(self):
        print(f'{self.name}, {self.phone}, {self.address}')

#! AddressBook 클래스
# : 주소록 프로젝트의 모든 기능을 구현하는 클래스
# : 신규 주소록 등록, 수정, 삭제, 검색, 전체 출력 기능
#   + CSV 파일 읽기/쓰기
# - 여러 개의 Person 객체를 저장하는 리스트 포함
class AddressBook:
    # 생성자
    # : csv 파일을 읽어서 address_list 배열(리스트)에 저장
    # : 리스트 생성 후 csv 파일을 읽어오는 file_reader() 메서드를 호출
    def __init__(self):
        self.address_list = []
        self.file_reader() # CSV 파일 읽기 함수 실행 (인스턴스 메서드)
        
    # file_reader() 메서드
    # : CSV 파일('addressBook.csv')을 읽고 address_list 리스트에 데이터를 저장
    def file_reader(self):
        try:
            # 예외의 가능성이 있는 코드 블럭 작성
            # : 예외 발생 시 except / 발생하지 않으면 else 문 실행
            
            # >> 외부 프로그램과의 연결 시 사용
            file = open('addressBook.csv', 'rt', encoding='utf-8', errors='replace')
        except:
            # csv 파일이 없는 경우
            print('addressBook 파일이 없습니다.')
        else:
            # csv 파일이 있는 경우
            
            # 파일의 각 줄을 순회 후 공백 제거 & 콤마 분리
            # 이름,전화번호,주소
            # 이승아,0101111,연제구
            # 이도경,0102222,동래구
            # 김명진,0103333,부산진구
            for buffer in file:
                if buffer.strip():
                    # 공백 라인 건너뛰기
                    # 쉼표로 데이터 분리
                    name, phone, address = buffer.strip().split(',')
                    # 리스트에 추가
                    self.address_list.append(Person(name, phone, address))
            print('addressBook.csv 파일을 로드하였습니다.')
            file.close() # 파일 닫기
            
    # file_generator() 메서드
    # : address_list 리스트의 데이터를 사용하여 새로운 csv 파일 생성
    def file_generator(self):
        try:
            file = open('addressBook.csv', 'wt', encoding='utf-8')
            
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
            
        else:
            # 리스트에 있는 모든 주소록 데이터를 파일에 저장
            for person in self.address_list:
                file.write(f'{person.name},{person.phone},{person.address}\n')
            file.close()
            
    # menu() 메서드 (정적 메서드 - @staticmethod)
    # : 프로그램에서 수행할 작업 목록을 출력하고 사용자의 선택을 입력받음
    @staticmethod
    def menu():
        print('-' * 30)
        print('1. 신규 주소록 등록')
        print('2. 기존 주소록 수정')
        print('3. 기존 주소록 삭제')
        print('4. 주소록 검색')
        print('5. 전체 주소록 출력')
        print('0. 프로그램 종료')
        print('-' * 30)
        
        choice = int(input('수행할 작업을 숫자로 입력하세요: '))
        return choice # 입력값 반환
    
    # exit() 메서드
    # : 프로그램을 종료하는 기능 수행
    # : sys 모듈의 exit() 메서드를 호출
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()
        
    # run() 메서드
    # : 프로그램 실행 (메뉴 출력 & 사용자의 입력값에 따라 기능 실행(각 메서드 호출))
    def run(self):
        while True:
            choice = AddressBook.menu()  # 정적메서드 호출: 클래스명.메서드명()
            if choice == 0: self.exit()
            elif choice == 1: self.insert()
            elif choice == 2: self.update()
            elif choice == 3: self.delete()
            elif choice == 4: self.search()
            elif choice == 5: self.print_all()
            else: print('없는 번호입니다. 확인 후 다시 입력해주세요.')
            
    # insert() 메서드: 새로운 주소록 정보 추가
    def insert(self):
        print('== 신규 주소록 생성 ==')
        name = input('등록할 이름 입력: ')
        phone = input('등록할 전화번호 입력: ')
        address = input('등록할 주소 입력: ')
        
        if name and phone and address:
            # 모든 값이 입력된 경우
            self.address_list.append(Person(name, phone, address))
            self.file_generator() # 파일 업데이트
            print('신규 주소록이 정상적으로 생성되었습니다.')
        else:
            print('입력값이 부족하여 주소록이 생성되지 않았습니다.')
    
    # update() 메서드: 입력한 이름의 전화번호 & 주소 수정
    
    # delete() 메서드: 입력한 이름을 주소록에서 찾아 삭제
    
    # search() 메서드: 입력한 이름의 주소록을 출력
    
    # print_all() 메서드: 전체 주소록 정보를 출력