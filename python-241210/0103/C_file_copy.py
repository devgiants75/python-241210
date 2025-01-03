# C_file_copy

# 1. 파일 복사
# : 원본 파일(source)의 복사본 파일(copy)을 만드는 것

# 2. 파일 복사의 절차
# - 원본 파일 열기
# - 복사본 파일 생성
# - 원본 파일의 내용 읽기 & 복사본 쓰기
# : 원본 파일에서 한 번에 읽어들이는 데이터 크기를 1KB(1024Byte)로 설정
#       , 복사 프로그램 구현
# - 파일 닫기 (with문 사용 시 생략 가능)

# cf) 픽사베이: 무료 이미지/동영상 다운로드 사이트

# dog-5357794_1280.jpg (원본 파일명)

image_size = 1024 # 1024byte == 1KB

# 1. 원본 파일 열기
# cf) 모드 - 파일 종류: t(text), b(binary, 이미지, 동영상)
with open('dog-5357794_1280.jpg', 'rb') as source:
    # 2. 복사본 파일 생성
    with open('copy_dog.jpg', 'wb') as copy:
        # 원본 파일을 처음부터 끝까지 반복하여 복사본 파일에 첨부
        while True:
            # read(파일의 용량 지정)
            buffer = source.read(image_size)
            if not buffer: # 버퍼가 비워진 경우: 즉 원본 파일을 모두 읽어온 경우
                break

            copy.write(buffer)
print('copy_dog.jpg 파일이 생성되었습니다.')
            
