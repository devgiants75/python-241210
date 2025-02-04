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
    time.sleep(5)
    
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
    time.sleep(5)
    
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
    
#! 웹 크롤링한 데이터를 활용하여 데이터 시각화
# : matplotlib 라이브러리 사용

#? 제목의 길이 계산
# : titles 배열을 순회하여 각 제목을 title 변수에 담고
#   , 제목의 길이를 title_lengths 변수의 요소로 저장
title_lengths = [len(title) for title in titles]

# 데이터 시각화
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# 히스토그램(Histogram) 생성
# : 막대 그래프와 유사한 그래프
# - 데이터의 분포를 시각적으로 표현하는 그래프
# >> 연속적인 데이터를 시각화 시 사용
plt.hist(title_lengths, bins=10, edgecolor='black', alpha=0.7)
# bins=10
# : 데이터를 10개의 구간(bin)으로 나누어 히스토그램을 그림
# alpha=0.7
# : 막대의 투명도를 조절 (0은 완전 투명, 1은 완전 불투명)

plt.title('Distribution of Video Title Lengths', fontsize=16)
plt.xlabel('Title Length', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# y축에 그리드 추가 (점선 형태)
# : 그래프의 보조선을 추가하는 함수
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()