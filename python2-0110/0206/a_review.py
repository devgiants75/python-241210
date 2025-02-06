# a_review.py

### matplotlib을 활용한 데이터 시각화 ###

# Counter 모듈 사용
# : 데이터의 빈도 수를 계산
# : 이터러블(iterable, '리스트', '튜블', '문자열 ' 등) 데이터의 각 요소가 얼마나 자주 있는지 계산
# > 변수 = Counter(이터러블 데이터)
from collections import Counter

# 포켓몬 데이터를 리스트로 정의
pokemon_data = [
    (1, "이상해씨", "풀/독"), # 포켓몬 번호, 이름, 타입
    (2, "이상해풀", "풀/독"),
    (3, "이상해꽃", "풀/독"),
    (4, "파이리", "불꽃"),
    (5, "리자드", "불꽃"),
    (6, "리자몽", "불꽃/비행"),
    (7, "꼬부기", "물"),
    (8, "어니부기", "물"),
    (9, "거북왕", "물"),
    (10, "캐터피", "벌레"),
    (11, "단데기", "벌레"),
    (12, "버터플", "벌레/비행"),
    (13, "뿔충이", "벌레/독"),
    (14, "딱충이", "벌레/독"),
    (15, "독침붕", "벌레/독"),
    (16, "구구", "노말/비행"),
    (17, "피죤", "노말/비행"),
    (18, "피죤투", "노말/비행"),
    (19, "꼬렛", "노말"),
    (20, "레트라", "노말"),
    (21, "깨비참", "독"),
    (22, "독파리", "독/비행"),
    (23, "아보", "독"),
    (24, "아보크", "독"),
    (25, "피카츄", "전기"),
    (26, "라이츄", "전기")
]