# d_library_review.py

### 웹 크롤링 & 엑셀 관리 ###
#! : 셀레니움(Selenium)과 Pandas를 사용
# >> 네이버 스포츠(Naver Sports) 데이터를 크롤링하고 엑셀 파일로 저장

'''
네이버 메인 페이지에서 특정 키워드로 검색 후 기사 목록 크롤링
기사 제목, 링크, 작성일을 수집
엑셀 파일로 저장 (naver_search_aespa.xlsx)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd