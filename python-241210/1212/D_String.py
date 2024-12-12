# D_String

# === 파이썬 문자열 구조 확인 === #
message = "I like you!"

# 1. 문자열 길이(Length)
# : len(길이를 구하고자 하는 문자열)
# : 문자열 길이를 구하는 파이썬 내장 함수(기능)
# : 띄어쓰기(공백)와 기호를 문자로 포함
print(len(message)) # 11

# 2. 문자열 인덱싱
# : 문자열 내의 특정 위치에 있는 문자에 접근하는 방법
# : 인덱스 번호는 0부터 시작(왼쪽)
#       +) 문자열 끝에서 시작하는 경우 -1 부터 시작
# cf) index: 표시

# 문자열 내의 마지막 문자의 인덱스 번호: 문자열 길이 - 1

# 문자열 인덱싱 방법
# : 변수명[인덱스번호]
print(message[0]) # 첫 번째 I
print(message[5]) # 여섯 번째 e
print(message[10]) # 열한 번째 !
print(message[-1]) # 마지막 !

# 3. 문자열 슬라이싱(slicing)
# : 문자열 안의 단어(부분 문자열)를 뽑아내는 역할
# 슬라이싱 방법
# : 변수명[시작번호:끝번호]
# >> 시작 번호, 끝 번호: 문자의 인덱스 번호를 사용
# >> 시작 번호는 포함 O, 끝 번호는 포함 X

# message = "I like you!"
print(message[2:6]) # like
print(message[0:6]) # I like
print(message[7:10]) # you

# cf) 처음부터 슬라이싱하거나 끝까지 슬라이싱하는 경우
#       : 시작과 끝 번호 생략 가능

print(message[:6]) # I like
print(message[7:]) # you!

# 끝자리 부터 추출(-1 부터 시작)
print(message[-1:-4]) # you!

# 파일 이름에서 확장자 추출
file_name = "document.pdf"
print("파일 확장자: ", file_name[-3:]) # pdf