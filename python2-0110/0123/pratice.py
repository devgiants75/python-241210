
### 웹 크롤링 실습 ###

# Wikipedia의 메인 페이지에서 오늘의 주요 기사 제목 가져오기

import requests
from bs4 import BeautifulSoup

# Wikipedia 메인 페이지의 URL

#? https://en.wikipedia.org/wiki/Main_Page
url = "https://en.wikipedia.org/wiki/Main_Page"

# HTTP GET 요청
response = requests.get(url)

# HTTP 요청의 응답은 반드시 상태 코드를 가짐
if response.status_code == 200:
    # BeautifulSoup 라이브러리를 사용하여
    # response.text(응답 내의 웹 문서의 구조)를 html 형식으로 분석(parse)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 오늘의 주요 기사 제목 선택
    title = soup.select_one('#mp-tfa > p > b > a').text
    
    print(title)
    
else:
    print('잘못된 요청입니다.', response.status_code)
    # 403: 권한 X
    # 404: URL 경로가 잘못된 경우