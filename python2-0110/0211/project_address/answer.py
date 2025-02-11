# answer.py

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
            file.close()