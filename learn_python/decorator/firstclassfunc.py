# 2020.02.12
# First Class Function
# 참고 : http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8D%BC%EC%8A%A4%ED%8A%B8%ED%81%B4%EB%9E%98%EC%8A%A4-%ED%95%A8%EC%88%98-first-class-function/
# 기본개념은 함수를 인자로 전달하거나 다른 함수의 결과값으로 리턴하고, 함수를 변수에 할당하고, 데이터 구조에 저장할 수 있는 함수

def square(x):
    return x ** 2

f = square

print(square(5))  # 직접 호출과
print(f(5))       # 변수 할당 후 호출 결과가 같고.
print(square)     # 기존 함수와
print(f)          # 변수 할당 된 함수가 동일한 square 함수임을 알 수 있다.

# 이러한 기능을 활용하여 wrapper 함수를 만들어 함수의 결과를 변수에 할당해서 필요할때 바로 사용할 수 있다.
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def quad(x):
    return x ** 4
def wrapper(func, arg_list):
    return [func(i) for i in arg_list]

num_list = [1, 2, 3, 4, 5]

squares = wrapper(square, num_list)
cubes = wrapper(cube, num_list)
quads = wrapper(quad, num_list)

print(squares)
print(cubes)
print(quads)

# 값이 아닌 다른 함수를 리턴하는 방법도 있다.
def logger(msg):
    def log_message():
        print('logger >> ', msg)
    return log_message

log_hi = logger('Hi')
print(log_hi)
log_hi()
del logger  # 글로벌 네임스페이스에서 logger 함수를 지워도
try:
    print(logger)
except NameError:
    print('NameError: name \'logger\' is not defined')
log_hi()    # 클로저 덕분에 아직 로그가 찍힙니다.

# 간단한 예시를 통해 다시 한번 정리 해 봅니다.
# 기존에는 아래와 같은 방식으로 함수를 만들어 사용했습니다.
def simple_html_tag(tag, msg):
    print('<{0}>{1}<{0}>'.format(tag, msg))

simple_html_tag('h1', '심플 헤딩 타이틀')

print('-'*30)

# 함수를 리턴하는 함수를 활용하면 아래와 같은 코드로 변경해서 실행 해볼 수 있습니다.
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print(print_h1)  # wrap_text 함수가 들어있는 것을 확인 할 수 있습니다.
print_h1('h1 태그를 활용한 메시지')

print_p = html_tag('p')
print_p('p 태그 메시지')
