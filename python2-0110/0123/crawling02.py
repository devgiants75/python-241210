# crawling02.py

### 웹 크롤링 환경 설정 가이드 ###

#! 1. 웹 브라우저
# : 크롬, 파이어폭스, 사파리, 엣지 등 

# cf) 크롬 사용 - 개발자 도구

#! 2. requests 라이브러리
# : 사용자가 서버에 요청하는 requests를 쉽게 수행하는 라이브러리
# - 웹 페이지의 HTML(웹 문서)을 가져오는 데 사용
#       : 웹 문서 구조를 가져옴
# - 명령어를 사용하여 설치
# a. 명령 프롬프트(cmd) 또는 터미널 엽니다.
# b. pip install requests (설치 명령어를 입력합니다.)
# c. pip list 명령어를 입력하여 requests 설치 확인

#! 3. BeautifulSoup 라이브러리
# : 웹 문서의 구문을 분석하여 필요한 내용만 추출할 수 있는 기능을 가진 라이브러리
# - 명령어를 사용하여 설치
#       : pip install BeautifulSoup4

#! 4. 크롬 개발자 도구 사용
# - 개발자 도구 여는 방법
# a. 원하고자 하는 웹 페이지에서 오른쪽 마우스 클릭 > '검사' 클릭
# b. f12