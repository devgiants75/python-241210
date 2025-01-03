# review02

# 파이썬 종합 문제 - 변수, 연산, 반복문, 조건문, 컬렉션 타입, 사용자 입력 처리 등 #

### 사용자 평점 기반 영화 추천 시스템 ###

# 요구사항 #
# 1. 사용자로부터 영화 평점 입력받기
# 2. 영화의 수는 최대 5개, 각 영화에 대한 평점 1 ~ 5 입력
# 3. 평균 평점이 가장 높은 영화를 찾아 출력
# 4. 만약 사용자가 영화 평점을 잘못 입력하면(1 ~ 5 사이의 범위를 벗어남)
#       오류 메시지를 출력하고 다시 입력받기

def get_movie_ratings():
    movie_ratings = {} # 딕셔너리 - 영화명(키), 평점(값)
    number_of_movies = int(input("입력할 영화의 수를 입력하세요. (최대 5개)"))

    # 사용자가 지정한 영화 수 또는 최대 5개를 입력 - 반복
    for i in range(min(number_of_movies, 5)): # range(N): 0부터 N미만까지 반복 - N번 반복
        # number_of_movies와 숫자 5 중에서 더 작은 값의 수로 반복
        movie_name = input(f'영화 {i + 1}의 이름을 입력하세요.')

        rating = 0 # 평점을 담을 변수 선언

        while rating < 1 or rating > 5:
            rating = int(input(f'{movie_name}에 대한 평점을 입력하세요 (1 ~ 5)'))
            if rating < 1 or rating > 5:
                print('평점은 1에서 5사이어야 합니다. 다시 입력하세요.')

        movie_ratings[movie_name] = rating # 딕셔너리명[키] = 값
    return movie_ratings

def recommend_movies(movie_ratings):
    if not movie_ratings: # 평가된 영화가 없을 경우
        print('추천할 영화가 없습니다.')
        return

    # 딕셔너리명.values(): 값들이 리스트 형태로 반환
    highest_rating = max(movie_ratings.values())
    recommend_movies = [
        movie for movie, rating in movie_ratings.items() # 키와 값을 리스트 형태로 반환
        if rating == highest_rating
    ]

    print('추천 영화: ' + ", ".join(recommend_movies))

movie_ratings = get_movie_ratings()
recommend_movies(movie_ratings)