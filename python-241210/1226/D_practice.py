# D_practice

string1 = "a b a c a a d a c"

# 1. a의 개수 구하기: count()
print(string1.count('a')) # 5

# 2. 문자열에서 c가 처음으로 등장하는 위치를 출력
# .find(), .index()
print(string1.find('c'))
print(string1.index('c'))

# 3. 문자열의 제일 첫 문자만 대문자로 변경
# .capitalize()
print(string1.capitalize()) # A b a c a a d a c

# 4. " Hello, World "의 양쪽 공백을 제거하고
#       ', '를 기준으로 분리하여 리스트로 저장
message = " Hello, World "
no_strip = message.strip()
list_change = no_strip.split(', ')
print(list_change) # ['Hello', 'World']