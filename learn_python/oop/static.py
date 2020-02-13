# 2020.02.13
# Static and class method (200~206)

# Instance 하지 않고도 바로 사용할 수 있는 static
class String:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        s = ''.join(c for c in s if c.isalnum())
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

print(String.is_palindrome('Radar', case_insensitive=False))
print(String.is_palindrome('A nut for a jar of tuna'))
print(String.is_palindrome('Never Odd, Or Even!'))
print(String.is_palindrome('In Girum Imus Nocte Et Consumimur Igni'))
print(String.get_unique_words('I love palindromes. I really really love them!'))

print('-'*30)
# class method는 호출 된 클래스의 attr를 가지고 동작함
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)

p = Point.from_tuple((3, 7))
print(p.x, p.y)
q = Point.from_point(p)
print(q.x, q.y)

# 이 예제로 이해가 잘 안가서 추가 예제 학습함
# 참고:https://hamait.tistory.com/635
class Date:
    word = 'date: '

    def __init__(self, date):
        self.date = self.word + date

    @classmethod
    def class_now(cls):
        return cls("today")

    @staticmethod
    def static_now():
        return Date("today")

    def show(self):
        print(self.date)

class KorDate(Date):
    word = '날짜: '

d = KorDate.class_now()
d.show()  # classmethod 지정 안하면 Date함수의 word 값인 'date: ' 기준으로 값이 출력된다!
d = KorDate.static_now()
d.show()

print('-'*30)

# Private method and name mangling
# 파이썬에는 private 개념이 없기 때문에 name mangling을 통해 비슷하게 사용한다.

class PrivateA:
    def __init__(self, factor):
        self._factor = factor

    def operateA(self):
        print('Operate 1 with factor ', self._factor)

class PrivateB(PrivateA):
    def operateB(self, factor):
        self._factor = factor
        print('Operate 2 with factor ', self._factor)

obj = PrivateB(100)
obj.operateA()
obj.operateB(42)
obj.operateA()    # A의 self.factor 값이 B에 의해 건드려져버림
print(obj.__dict__.keys())

# 참 별거 아닌 것 같지만 앞에 underscore 두 개 붙여주면 해결이 된다.
class PrivateA:
    def __init__(self, factor):
        self.__factor = factor

    def operateA(self):
        print('Operate 1 with factor ', self.__factor)

class PrivateB(PrivateA):
    def operateB(self, factor):
        self.__factor = factor
        print('Operate 2 with factor ', self.__factor)

obj = PrivateB(100)
obj.operateA()
obj.operateB(42)
obj.operateA()
print(obj.__dict__.keys())
