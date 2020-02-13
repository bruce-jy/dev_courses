# 2020.02.13
# OOP에서 Class 관련 (182~187)

class Person:
    species = 'Human'

print(Person.species)
Person.alive = True
print(Person.alive)  # 동적으로 값을 추가할 수 있다.

print('-'*30)

man = Person()
man.species = 'Huuuuuman'
man.name = 'John'
print(man.species)     # man의 species만 업데이트 되고
print(Person.species)  # Person의 species는 업데이트 안됌
print(man.name)
try:
    print(Person.name)  # man instance에만 name을 추가했기 때문에 Person에는 name attr가 없어 오류발생.
except AttributeError:
    print('man instance에만 name을 추가했기 때문에 Person에는 name attr가 없어 오류발생.')

print('-'*30)

class Square:
    side = 8

    def area(self):  # self는 해당 클래스 인스턴스의 참조를 의미한다.
        print(self)
        return self.side ** 2

sq = Square()
print(sq.area())        # 이미 생성된 인스턴스에는 self를 넘기지 않아도 실행가능
print(Square.area(sq))  # 인스턴스 생성 안된 클래스의 함수를 호출할땐 self에 해당하는 인스턴스 전달 필요
print(Square().area())  # <-- 새로 인스턴스를 생성하면 참조값이 다름
sq.side = 10
print(sq.area())
print(Square.area(sq))

print('-'*30)

# 인스턴스 초기화 __init__
class Rectangle:
    def __init__(self, sideA = 4, sideB = 4):  # 여기서 기본값 설정 가능
        self.sideA = sideA
        self.sideB = sideB

    def area(self):
        return self.sideA * self.sideB

r1 = Rectangle(10, 4)  # 10과 4로 초기화 한다.
print(r1.sideA, r1.sideB)
print(r1.area())

r2 = Rectangle()
print(r2.sideA, r2.sideB)

print('-'*30)

