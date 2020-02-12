# 2020.02.12
# Decorators(173~181)

# 앞서 배웠던 first class function 방식으로 사용하면 아래와 같은 방식으로 코드 활용이 가능합니다.
def decorator(f):
    def wrapper():
        print(f.__name__, 'decorator')
    return wrapper

def func():
    pass  # 실행할 코드 없음
func = decorator(func)
func()

# 동일한 함수를 decorator (@함수명)을 활용해서 작성하면 아래와 같이 작성할 수 있습니다.
@decorator
def func():
    pass
func()

# 함수명은 어떤 것을 적어도 상관 없고, @뒤에 함수명만 붙여주면 decorator가 실행됩니다.
# 여러 함수를 사용할 수도 있습니다.
print('decorator 여려개 사용하기', '-' * 30)
from functools import wraps
def deco1(f):
    def wrapper():
        print(f.__name__, 'deco 1 print')  # <-- 여기서 함수명이 wrapper로 나오게 된다.
        return f()
    return wrapper

def deco2(f):
    @wraps(f)  # 위의 f.__name__이 wrapper로 나오는 문제를 해결하기 위해 wraps()를 사용하면 deco1에게 deco2의 wrapper가 아닌 원래 func2를 넘겨줄 수 있다.
    def wrapper():
        print(f.__name__, 'deco 2 print')
        return f()
    return wrapper

@deco1
@deco2
def func2():
    print('func 2 print')

func2()

print('decorator 변수 넘겨서 사용하기', '-' * 30)
def deco_arg(arg1, arg2):
    def wrapper(f):
        def inner_wrapper():
            print(f.__name__, 'arg1={}, arg2={}'.format(arg1, arg2))
        return inner_wrapper
    return wrapper

@deco_arg(1, 'test')
def func3():
    print('func 3')

func3()

print('decorator factory', '-' * 30)
def max_result(threshold):
    def decorator(calc_func):
        @wraps(calc_func)
        def wrapper(*args, **kwargs):
            result = calc_func(*args, **kwargs)
            if result > threshold:
                print('Result it too big({0}). Max allowed is {1}.'.format(result, threshold))
                return threshold
            else:
                return result
        return wrapper
    return decorator

@max_result(100)
def cube(n):
    return n ** 3

@max_result(100)
def adder(a, b):
    return a + b

print(cube(5))
print(adder(50, 51))

print('----실전 코드 활용법1 - Class의 Method decorating 하기----')
# 실전 코드 활용법1 - Class의 Method decorating 하기
# 참고 : https://medium.com/sjk5766/%EB%B2%88%EC%97%AD-python%EC%9D%98-%ED%95%A8%EC%88%98-decorators-%EA%B0%80%EC%9D%B4%EB%93%9C-2cd9d5151a1d
def name_decorator(origin_func):
    def wrapper(*args, **kwargs):
        print(origin_func.__name__, args, kwargs)
        return "<span class='pName'>{0}</span>".format(origin_func(*args, **kwargs))
    return wrapper

class Person(object):
    def __init__(self):
        self.name = 'John'
        self.family = 'Doe'

    @name_decorator
    def get_fullname(self):
        return self.name + ' ' + self.family

my_person = Person()
print(my_person.get_fullname())

print('----실전 코드 활용법2 - Tag wrapper 만들기----')
# 실전 코드 활용법2 - Tag wrapper 만들기
# 참고 : https://medium.com/sjk5766/%EB%B2%88%EC%97%AD-python%EC%9D%98-%ED%95%A8%EC%88%98-decorators-%EA%B0%80%EC%9D%B4%EB%93%9C-2cd9d5151a1d
def html_tag(tag_name):
    def tag_generator(tag_func):
        print(tag_func.__name__)

        @wraps(tag_func)
        def wrapper(text):
            return '<{0}>{1}</{0}>'.format(tag_name, tag_func(text))
        return wrapper
    return tag_generator

@html_tag('div')
@html_tag('p')
@html_tag('span')
def get_text(text):
    return text

print(get_text('test text in here'))
