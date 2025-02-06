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

# 포켓몬 타입 데이터를 분리 > 모든 타입 리스트를 생성
all_types = [] # 모든 타입을 담을 리스트 초기화

for _, _, types in pokemon_data: # poketmon_data의 각 항목에서 타입 정보를 추출 ("독/비행")
    type = types.split('/') # 슬래시('/')로 나뉜 타입을 리스트에 추가 (['독', '비행'])
    all_types.extend(type) # 한 번에 여러 요소를 리스트에 추가(확장)
    
# types = ["풀/독", "풀/독", "풀/독", "불꽃", "불꽃", "불꽃/비행", ... , "전기", "전기"]
# all_types = ["풀", "독", "풀", "독", "풀", "독", "불꽃", ... ... , "전기", "전기"]

# append() VS extend()

# append(): 리스트의 끝에 데이터를 그대로 삽입
x = [1, 2]
y = [3, 4]
x.append(y) # [1, 2, [3, 4]]
print(x)

# extend(): 리스트의 끝에 해당 데이터의 '각' 항목을 삽입
x = [1, 2]
y = [3, 4]
x.extend(y) # [1, 2, 3, 4]
print(x)

# 타입별 포켓몬 수 계산
type_counts = Counter(all_types)
print(type_counts)
# Counter({'독': 10, '비행': 6, '벌레': 6, '노말': 5, '풀': 3, '불꽃': 3, '물': 3, '전기': 2})

#! matplotlib 라이브러리 사용 - 그래프 생성 

from matplotlib import font_manager, rc # 한글 폰트 설정
import matplotlib.pyplot as plt 
import matplotlib

# 한글 폰트 경로 설정
font_path = 'C:\\Windows\\Fonts\\H2PORM.TTF'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# 막대 그래프 데이터 #
types = list(type_counts.keys()) # 타입 이름 리스트
counts = list(type_counts.values()) # 타입별 포켓몬 수 리스트

# 막대 그래프 생성 #
plt.figure(figsize=(10, 6))
plt.bar(types, counts, color='skyblue', edgecolor='black')
plt.title('타입별 포켓몬 수', fontsize=16)
plt.xlabel('포켓몬 타입', fontsize=12)
plt.ylabel('포켓몬 수', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()