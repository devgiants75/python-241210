# d_library_review.py

### 웹 크롤링 & 엑셀 관리 ###
# !: 셀레니움(Selenium)과 Pandas를 사용
# >> 네이버 검색 데이터를 크롤링하고 엑셀 파일로 저장

'''
네이버 메인 페이지에서 aespa 키워드로 검색 후 기사 목록 크롤링
기사 제목, 링크, 작성일을 수집
엑셀 파일로 저장 (naver_search_aespa.xlsx)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 웹 드라이버 설정 (Chrome)
driver = webdriver.Chrome()

# 네이버 검색 페이지 접속
search_url = "https://search.naver.com/search.naver?query=aespa&where=news"
driver.get(search_url)

# 페이지 로딩 대기
time.sleep(2)

# 기사 정보 저장을 위한 리스트
news_list = []

# 기사 목록 크롤링
articles = driver.find_elements(By.CSS_SELECTOR, "ul.list_news > li")

for article in articles:
    try:
        # 기사 제목
        title_element = article.find_element(By.CSS_SELECTOR, "a.news_tit")
        title = title_element.text
        link = title_element.get_attribute("href")

        # 작성일
        date_element = article.find_element(By.CSS_SELECTOR, "span.info")
        date = date_element.text

        # 데이터 저장
        news_list.append([title, link, date])

    except Exception as e:
        print("오류 발생:", e)

# 웹 드라이버 종료
driver.quit()

# 데이터프레임 생성
df = pd.DataFrame(news_list, columns=["제목", "링크", "작성일"])

# 엑셀 파일로 저장
df.to_excel("naver_search_aespa.xlsx", index=False)

print("크롤링 완료: naver_search_aespa.xlsx 파일로 저장되었습니다.")