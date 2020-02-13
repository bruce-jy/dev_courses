# 2020.02.13
# Property decorator (206~208)
# 기존 언어들의 getter setter와 같은 역할을 하는 annotation

class Person:
    def __init__(self, age):
        self.age = age   # 이상태면 아무나 이 값을 바꿀 수 있음

class PersonWithAccessors:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18,99]')

class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18,99]')

person = PersonPythonic(39)
print(person.age)  # 똑같은 age 함수지만 getter로 동작한다.
person.age = 42
print(person.age)
try:
    person.age = 100  # 똑같은 age 함수지만 setter로 동작한다.
except ValueError:
    print('ValueError: Age must be within [18,99]')
