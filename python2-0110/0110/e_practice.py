### e_practice.py ###

import json

# 초기 데이터 설정
data = {
    "name": "이승아",
    "age": 50,
    "hobbies": ["운동", "독서"]
}

# json 파일로 저장
file_name = 'json_prac.json'
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f'{file_name} 파일이 생성되었습니다 :)')

# json 파일 읽기 & 수정
# 1) 파일 읽기(load 메서드 사용)
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)
    
# data 형식(딕셔너리 형식)
# : hobbies 키의 값(리스트)에 데이터 추가
# - 딕셔너리 자료 중 값에 접근: 딕셔너리명['키']
# - 딕셔너리 자료에 데이터 추가: append('값')

data['hobbies'].append('코딩')

# 2. 수정된 파일을 다시 json 파일에 저장
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
# 3. 수정된 파일 읽기 & 출력
with open(file_name, 'r', encoding='utf-8') as f:
    updated_data = json.load(f)
    
print(updated_data)

# 4. json 파일에서 특정 데이터 조회
# json 형식이 파이썬의 딕셔너리 형태와 유사
# : 데이터명[키]
print('Age ', data['age']) # 줄 복사: alt + shift + 방향키(위/아래)
print('Name ', data['name'])
print('Hobbies ', data['hobbies'])