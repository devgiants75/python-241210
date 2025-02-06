# b_faker.py

### faker 라이브러리 ###
# : 가짜 데이터를 생성하는 데 사용
# : 다양한 상황에서 테스트 데이터를 만들 때 유용
# > 외부 라이브러리 (설치 후 사용)
# > pip install faker, pip list

#! 사용 방법
from faker import Faker

# 기본 데이터 생성 - 영어로 작성
fake = Faker()

# 랜덤 이름 생성
print(fake.name())

# 랜덤 주소 생성
print(fake.address())

# 랜덤 이메일 생성
print(fake.email())

#! 한국어 데이터 생성
fake_ko = Faker('ko_KR')
print(fake_ko.name())
print(fake_ko.address())
print(fake_ko.phone_number())

#! 한 번에 여러 개의 데이터를 생성
for _ in range(10):
    print(fake_ko.name(), fake_ko.phone_number())
    
#! JSON 형태의 데이터 생성
# JSON: JavaScript Object Notation ( 자바스크립트 표준 객체 )

import json

data = [
    {
        "name": fake_ko.name(),
        "email": fake.email(),
        "address": fake_ko.address()
    }
    for _ in range(10)
]

# JSON 형식으로 출력
print(json.dumps(data, indent=4, ensure_ascii=False))