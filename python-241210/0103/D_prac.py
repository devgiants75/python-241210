# D_prac

### 파일 복사 예제 ###

# 이미지 파일 복사
# : 원본 이미지는 python-241210\outer 폴더 내에 저장
# : 복사본 이미지는 0103\inner 폴더 내에 저장

# 원본 이미지: C:\python-1210\python-241210\outer\cat-6723256_1280.jpg

image_size = 1024
with open('../outer/cat-6723256_1280.jpg', 'rb') as source:
    with open('./inner/copy_cat.jpg', 'wb') as copy:
        while True:
            buffer = source.read(image_size)
            if not buffer:
                break
            copy.write(buffer)

print('copy_cat.jpg 파일이 복사되었습니다.')