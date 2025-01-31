# b_naver_news.py

#! 웹 크롤링 시 사용자(데이터를 추출하고자 하는 사람) 정보 제공
# HTTP 헤더 (요청의 중심부 - 사용자의 정보를 전달, User-Agent)
# User-Agent 확인 방법
# : What is my user agent? 검색 > 사용자 컴퓨터 정보를 가져옴
# : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

from bs4 import BeautifulSoup
import requests

#? 네이버 뉴스 홈화면 URL
# https://news.naver.com/
url = 'https://news.naver.com/'

#? 사용자 정보를 헤더에 저장하여 제공
headerss = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headerss)
soup = BeautifulSoup(response.text, "html.parser")

news_list = soup.find_all('a', class_='cnf_news _cds_link _editn_link')

for news in news_list:
    title = news.text.strip() # strip(): 양쪽 공백 제거
    link = news['href']
    print(f'기사 제목: {title}, 링크: {link}')
