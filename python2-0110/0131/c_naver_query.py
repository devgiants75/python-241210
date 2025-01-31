# c_naver_query.py

### 검색 결과 웹 페이지 정보 가져오기 ###

# 네이버에서 '파이썬'을 검색한 결과 화면의 정보를 추출
# : 해당 결과 페이지의 URL
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC

#? 1. 기본 URL(Base URL)
# : 물음표 앞에 있는 URL
# : 요청되는 웹 페이지나 서비스를 식별
# - https://search.naver.com/search.naver

#? 2. 파라미터(parameter)
# : 사용자가 서버에게 요청하는 정보들이 전달되는 구역 (물음표 오른쪽)
# : '키=값' 쌍의 형태, 여러 개가 있는 경우 '&'로 구분
# - ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC
# - query 파라미터: naver에서 입력한 검색어를 저장하는 변수
#       >> query=파이썬

#! 네이버에서 '파이썬'을 검색한 결과 조회
# 1. 라이브러리 임포트
# : HTTP 요청 requests 라이브러리
import requests

# 2. 네이버 검색 URL과 검색어 파라미터 설정
url = 'https://search.naver.com/search.naver'
paramss = { 'query': '파이썬' }

# 3. HTTP 헤더 (사용자 정보 전달)
headerss = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url, params=paramss, headers=headerss, timeout=10)
# 타임아웃: 응답을 기다리는 최대 시간(초)
#   - 지정한 시간 내에 응답이 오지 않을 경우 timeout 오류 발생

print(f'Status Code: ${response.status_code}')
print(response.text)