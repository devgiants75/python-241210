# a_review.py

### 클래스 생성, 생성자, 소멸자 예제 ###

# 게임 구현
# 게임 캐릭터 - 객체로 생성
#   속성 - name, hp(hit point - 체력), strength(힘)
#   기능 - 공격 기능

#! 게임 캐릭터 클래스
# class 클래스명(UpperCamelCase):
    # 들여쓰기
class Character:
    # 인스턴스 변수 명시적 선언
    # name = ''
    
    # 생성자: 인스턴스 변수의 선언과 초기화를 담당
    # __init__(self, ...):
    def __init__(self, name, hp, strength):
        # 인스턴스 변수에 값을 할당: 인스턴스 변수의 생성과 초기화
        # 좌항: 인스턴스 변수
        # 우항: 인자값(실제 데이터)
        self.name = name
        self.hp = hp
        self.strength = strength
        print(f'캐릭터 {self.name}이 생성되었습니다.')
        print(f'체력은 {self.hp} / 힘은 {self.strength}입니다.')
        
    # 인스턴스 메서드
    def attack(self, other_character):
        # other_character: 매개변수(해당 클래스인 Character로 만들어진 또 다른 객체)
        print(f'{self.name}이(가) {other_character.name}을(를) 공격합니다.')
        # other_character.hp = other_character.hp - self.strength
        other_character.hp -= self.strength
        
    # 소멸자를 대신하는 인스턴스 메서드
    def remove_from_game(self):
        print(f'{self.name}이(가) 게임에서 사라졌습니다.')
        
# Character 클래스를 사용한 객체 생성
Son = Character('Son', 400, 150)
Naymar = Character('Naymar', 300, 40)

# 객체의 메서드 인자값으로 또 다른 객체를 전달
Son.attack(Naymar)
print(f'네이마르의 남은 체력은 {Naymar.hp}입니다.')

Son.attack(Naymar)
print(f'네이마르의 남은 체력은 {Naymar.hp}입니다.')

Naymar.attack(Son)
print(f'손흥민의 남은 체력은 {Son.hp}입니다.')

# 소멸자를 대신한 캐릭터 제거 메서드 실행
if Naymar.hp <= 0:
    Naymar.remove_from_game()
    del Naymar
    
# Naymar.attack(Son)
# >> Naymor 객체는 메모리에서 제거(읽혀지지 않음)