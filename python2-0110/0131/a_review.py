# a_review.py

#! Crawling(크롤링)
# : 웹 페이지에서 데이터를 추출하는 작업
# : 웹 크롤링, 데이터 크롤링으로 불림
# - 검색엔진에서 정보를 추출하는 데 사용
# - SEO(검색엔진 최적화) 및 검색 전략 수집에 필수적

# cf) Crawler(크롤러)
# : 크롤링을 수행하는 소프트웨어
# - 자동화된 프로그램으로 웹 사이트를 돌아다니며 정보를 추출

#? 웹 크롤링을 위한 라이브러리
# : 웹 크롤링을 수행하기 위해서는 웹 페이지 '요청'을 보내고
#       , '응답'받은 HTML(웹 문서)을 파싱(분석)하여 원하는 데이터를 추출

#& 1. 크롬(Chrome)을 활용
# : 개발자 도구(DevTools)를 사용하여 웹 페이지의 구조를 쉽게 분석
# : 크롤링에 필요한 요소(태그, 클래스 속성, ID 속성 등)를 쉽게 찾을 수 있음

# cf) 크롬 개발자 도구 활용법
# - f12 또는 ctrl + shift + i 
# - 지정 요소를 확인하는 방법: 요소위에 우클릭 >> 하단의 '검사(Inspect)' 클릭

# cf) 크롬 개발자 도구 기능
# - Elements(요소): HTML(웹 문서) 태그와 구조를 확인
# - Console(콘솔): JavaScript 실행 및 오류 확인 
# - Network(네트워크): 웹 요청 및 응답 확인
# - Application: 쿠키, 로컬 스토리지 확인 
# - Performane: 페이지 로딩 속도 분석

#& 2. requests 라이브러리
# : 웹 서버에 요청(request)을 보내고 응답(response)를 받아오는 라이브러리

# 1) 설치 방법 & 설치 확인
# : pip install requests
# : pip list

# 2) 사용법
# - 기본 GET 요청
import requests 

# url = "데이터를 추출하고자 하는 페이지 URL"
url = 'https://example.com'
response = requests.get(url) # GET 요청 수행

# - HTTP 응답 코드 확인
# : 200(성공), 403(접근 권한 X), 404(URL이 존재하지 X), 500(네트워크 오류)

if response.status_code == 200:
    print('요청 성공!')
elif response.status_code == 404:
    print('페이지를 찾을 수 없습니다.')
    
#& 3. BeautifulSoup4 라이브러리
# : HTML, XML을 파싱하여 원하는 데이터를 쉽게 추출하는 라이브러리
# - requests와 함께 사용됨

# 1) 설치 방법 & 설치 확인
# : pip install beautifulsoup4
# : pip list

# 2) 사용 방법
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser") # HTML 파싱

# HTML 구조 확인
soup.prettify()

# 특정 태그 선택
soup.title # <title> 태그 출력
soup.title.text # <title> 태그의 텍스트만 출력

# 특정 요소 찾기
# find(): 첫 번째로 발견된 요소 반환
# find_all(): 모든 요소 리스트로 반환
heading = soup.find('h1') # 첫 번째 h1 태그 찾기

all_paragraphs = soup.find_all('p') # 모든 p태그 찾기

# 클래스 또는 ID로 요소 찾기
# - 클래스 속성: 여러 요소에 붙이는 이름
div = soup.find('div', class_='content')

# - ID 속성: 단 하나의 요소에 붙이는 이름
section = soup.find(id='main-section')

#? 링크(a태그, anchor) 가져오기
for link in soup.find_all('a'):
    # a태그의 href 속성은 해당 요소 클릭 시 이동하는 페이지 URL
    # : link 객체의 href 속성으로 값을 추출
    print(link['href'])

#? 이미지 가져오기
for img in soup.find_all('img'):
    print(img['src'])