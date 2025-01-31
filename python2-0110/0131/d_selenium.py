# d_selenium.py

### 셀리니움을 활용한 웹 크롤링 ###

# requests: 웹 문서의 정보를 가져오는 요청을 위한 '라이브러리'
# BeautifulSoup: requests 라이브러리로 가져온 웹 문서에서 데이터를 추출하는 '라이브러리'
# Seleuium: 웹 페이지의 동적 데이터 크롤링과 사용자 이벤트 자동화 지원 '프레임워크'

# cf) 프레임워크(frame + work)
# : frame(틀) + work(일하다)
# - 제공받은 일정한 요소와 틀, 규약을 가지고 무언가를 만드는 일

#? 셀레니움 사용 이유
# : BeautifulSoup 보다 데이터 추출이 용이
# - 동적 페이지에서 틀과 별도로 호출된 정보를 추출, 사용자 이벤트까지 크롤링이 가능

#? 셀레니움 사용 방법
# : pip install selenium
# : pip list

#? 크롬 웹 드라이버 다운
# : https://developer.chrome.com/docs/chromedriver/downloads?hl=ko
# : https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.87/win64/chromedriver-win64.zip

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#? 셀레니움으로 브라우저 창 열기
# : 셀레니움으로 원하는 주소를 자동으로 실행하는 웹 브라우저 구동
options = Options() # Options 라이브러리 내의 기능을 호출하여 저장

# 크롬 드라이버 실행
driver = webdriver.Chrome(options=options)

url = 'https://www.naver.com'
driver.get(url)

# === 네이버 자동 검색 수행 ===
# 1. 네이버 메인 페이지 접속(www.naver.com)
# 2. 오른쪽 마우스 클릭 > 바로가기 메뉴 > [페이지 소스 보기] 클릭
# 3. ctrl + f: 검색창 열기
# 4. input 입력: 태그 검색
# <input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element/> 

# id 속성: 특정 태그를 지시하기 위해 사용되는 속성 (중복X)
# class 속성: 여러 태그를 하나로 지시하기 위해 사용되는 속성 (중복O)

from selenium.webdriver.common.by import By # 태그를 지시하기 위한 속성
from selenium.webdriver.common.keys import Keys # 키보드 입력값을 저장

# 5. id 값 확인 > 해당 태그 불러오기
# : find_element(By.ID, "id값")
query = driver.find_element(By.ID, 'query')

# 6. 해당 요소(태그)에 대한 작업 수행
# 1) send_keys(키 입력값): 키보드를 통한 키 입력
# 2) click(): 마우스를 통한 클릭

query.send_keys('파이썬') # 검색창에 '파이썬' 입력
query.send_keys(Keys.RETURN) # Enter 키 입력 (검색 실행)

input('...') # 검색 결과 확인을 위한 입력 대기 상태
driver.quit() # 브라우저 종료