# crawlingPractice02.py

# 필요한 라이브러리 import #

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
from wordcloud import WordCloud

import time
import matplotlib.pyplot as plt

# Selenium WebDriver 설정
# : 크롬 웹드라이버 옵션 설정
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

# 네이버 검색 페이지로 이동
naver_search_url = "https://www.naver.com"
driver.get(naver_search_url)
time.sleep(2) # 페이지 로드 대기

# 검색창에 "서면 맛집" 입력 및 검색
search_box = driver.find_element(By.NAME, "query") # 네이버 검색창 요소 찾기
search_box.send_keys("서면 맛집") # 검색창에 "서면 맛집" 입력
search_box.send_keys(Keys.RETURN) # Enter 키를 눌러 검색 실행
time.sleep(2) # 검색 결과 페이지 로드 대기

# 페이지 소스 가져오기
page_source = driver.page_source # 현재 페이지의 HTML 소스 가져오기
driver.quit() # 드라이버 종료

# BeautifulSoup로 HTML 파싱
soup = BeautifulSoup(page_source, "html.parser")

# 검색 결과에서 텍스트 데이터 추출
titles = soup.select(".title") # 제목에 해당하는 클래스 이름
descriptions = soup.select(".api_txt_lines") # 설명에 해당하는 클래스 이름

text_data = " ".join([title.get_text() for title in titles])
text_data += " " + " ".join([desc.get_text() for desc in descriptions])

# 워드 클라우드 생성
# : WordCloud 라이브러리를 사용하여 워드 클라우드를 생성
wordCloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    colormap="viridis",
    max_words=100,
    font_path="C:\\Windows\\Fonts\\HMKMRHD.TTF"
).generate(text_data)

# 워드 클라우드 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis("off")
plt.title("서면 맛집 워드 클라우드", fontsize=20)
plt.show()