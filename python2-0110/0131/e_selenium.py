# e_selenium.py

### 셀레니움을 사용하여 뉴스 제목을 자동으로 추출 ###

# 뉴스 제목의 태그와 속성 파악
# : 네이버 메인 화면 > kpop 검색 > 개발자 도구 열기(f12)

# <a href="http://starin.edaily.co.kr/news/newspath.asp?newsid=01269366642043296" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws_all*a.tit&amp;r=1&amp;i=880000E7_000000000000000005934040&amp;g=018.0005934040&amp;u='+urlencode(this.href));" title="투어스, 美 빌보드 선정 '이달의 K팝 루키'">투어스, 美 빌보드 선정 '이달의 K팝 루키'</a>

# class 속성
# : 여러 요소에 같은 이름을 사용
# - 드라이버.find_elements(By.CLASS_NAME, '클래스명')

# cf) id 속성: 드라이버.find_element(By.ID, 'id 명')

from selenium import webdriver # 브라우저를 자동으로 제어하는 객체
from selenium.webdriver.common.by import By # HTML 요소를 찾기 위한 방법을 제공하는 클래스
from selenium.webdriver.common.keys import Keys #키보드 입력을 자동으로 실행할 수 있도록 지원하는 클래스
from selenium.webdriver.chrome.options import Options # 브라우저에 옵션 상태 전달

options = Options()
driver = webdriver.Chrome(options=options)
url = 'https://www.naver.com'
driver.get(url) # 해당 url의 환경을 webdriver를 사용하여 실행

query = driver.find_element(By.ID, 'query')
query.send_keys('kpop')

query.send_keys(Keys.RETURN) # 엔터 키 입력

news_tit = driver.find_elements(By.CLASS_NAME, 'news_tit')
for title in news_tit:
    print(title.text)
    
input('...') # selenium을 사용한 웹 크롤링 후 곧바로 브라우저가 종료되는 것을 방지
driver.quit

# 터미널 종료 단축키: ctrl + c