# answer.py

import csv
import matplotlib.pyplot as plt

#! 날씨 데이터를 관리하는 클래스 정의
class WeatherDataManager:
    # 생성자
    def __init__(self, filename):
        self.filename = filename
    
    # 데이터 생성
    def create_data(self, city_name, date, max_temp, min_temp, rainfall):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file) # CSV 작성 객체 생성
            writer.writerow([city_name, date, max_temp, min_temp, rainfall])
    
    # 데이터 조회
    def read_data(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # 각 행을 반복하면서 출력
                print(row)
            
    # 데이터 수정
    def update_date(self, city_name, date, new_data):
        data = self._load_data()
        
        for row in data:
            if row[0] == city_name and row[1] == date:
                row[2:] = new_data
        self._save_data(data) # 수정된 데이터를 다시 파일에 저장
            
    # 데이터 삭제
    def delete_data(self, city_name, date):
        data = self._load_data()
        
        data = [row for row in data if not (row[0] == city_name and row[1] == date)]
        # : 삭제하고자 하는 특정 데이터를 제외한 요소들을 다시 리스트로 저장
        
    # CSV 파일에서 모든 날씨 데이터 불러오기
    def _load_data(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader] # 파일의 모든 행을 리스트 형태로 반환
        
    # 수정된 날씨 데이터를 CSV 파일에 다시 저장하기
    def _save_data(self, data):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data) # 데이터의 모든 행을 파일에 저장
            
#! 날씨 데이터를 시각화하는 클래스 정의
class WeatherVisualization:
    @staticmethod
    def visulaize(data):
        city_names = set(row[0] for row in data)
        
        
#! 프로그램 실행 함수 정의
def main():
    filename = 'weather_data.csv'
    weather_manager = WeatherDataManager(filename)
    
    while True:
        print('=== Enter command ===')
        command = input('create / read / update / delete / visualize / exit: ')
        
        if command == 'create':
            city_name = input('도시명을 입력하세요.')
            date = input('날짜를 입력하세요. (YYYY-MM-DD)')
            max_temp = input('최고 기온을 입력하세요.')
            min_temp = input('최저 기온을 입력하세요.')
            rainfall = input('강수량을 입력하세요.')
            
            weather_manager.create_data(city_name, date, max_temp, min_temp, rainfall)
        
        elif command == 'read':
            weather_manager.read_data()
        elif command == 'update':
            city_name = input('도시명을 입력하세요.')
            date = input('날짜를 입력하세요. (YYYY-MM-DD)')
            new_data = input('수정할 최고/최저 기온과 강수량을 콤마로 구분하여 입력하세요.').split(',')
            
            weather_manager.update_date(city_name, date, new_data)
        elif command == 'delete':
            city_name = input('도시명을 입력하세요.')
            date = input('날짜를 입력하세요. (YYYY-MM-DD)')
            
            weather_manager.delete_data(city_name, date)
        elif command == ' visualize':
            data = weather_manager._load_data() # CSV 데이터 로드
            WeatherVisualization.visulaize(data)
        elif command == 'exit':
            break
        else:
            print('Invalid Command')
            
main()