# z_prac.py
### 셀레니움을 활용한 데이터 크롤링 ###

# 유튜브 > christmas 검색 > 검색 결과에서 video 제목 추출 후 출력
# https://www.youtube.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)
url = 'https://www.youtube.com'
driver.get(url)

# By
# : 요소 검색 기능의 클래스
# : ID, CLASS_NAME, NAME, CSS_SELECTOR 등
# - 검색창: By.NAME, 'search_query'
# - 비디오 제목: By.CLASS_SELECTOR, '#video-title'