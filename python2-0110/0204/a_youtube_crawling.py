# a_youtube_crawling.py

### 셀레니움을 활용한 데이터 크롤링 ###

# 유튜브 > 검색창 'Christmas' 검색 > 검색 결과에서 video(영상) 제목 추출
# https://www.youtube.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options() # 크롬 옵션 설정

driver = webdriver.Chrome(options=chrome_options) # 크롬 드라이버 실행

import time

try:
    # 유튜브 웹 사이트 열기(접속)
    driver.get('https://www.youtube.com')
    
    # 페이지 로딩을 위한 대기 시간 설정 (2초)
    time.sleep(2)
    
    # 검색창 찾기
    # : HTML의 input 태그에서 name 속성이 'search_query'인 요소를 찾음
    # <input name="search_query" type="text" autocomplete="off" autocorrect="off" aria-autocomplete="list" role="combobox" class="ytSearchboxComponentInput yt-searchbox-input title" placeholder="검색">
    
    # By
    # : 요소 검색 기능의 클래스
    # - ID, CLASS_NAME, NAME, CSS_SELECTOR 등
    # >> 검색창: By.NAME, 'search_query'
    # >> 비디오 제목: By.CLASS_SELECTO, '#video-title'
    search_box = driver.find_element(By.NAME, 'search_query')
    search_keyword = 'christams'
    
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)
    
    # 검색 결과 로딩을 위한 대기 시간 설정 (2초)
    time.sleep(2)
    
    # CSS 셀렉터를 사용하여 '#video-title' 아이디를 가진 요소를 모두 선택
    # By.CSS_SELECTOR의 경우 값에 id는 #을, class는 .를 붙여 작성
    video_titles = driver.find_elements(By.CSS_SELECTOR, '#video-title')
    
    print(f"'{search_keyword}' 검색결과")
    
    # 빈 배열 작성 - 크롤링한 데이터를 저장할 빈 리스트
    titles = []
    for idx, title in enumerate(video_titles, start=1):
        print(f"{idx} - {title.text}")
        
        # 리스트에 제목 저장
        titles.append(title.text)

finally:
    driver.quit()