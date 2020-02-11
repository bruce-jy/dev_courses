# 2020.02.11
# Functions (101~134)

# 1. Variable positional arguments *로 tuple 변수를 동적할당할 수 있음
def func1(*args):
    print(args)
values = (1, 3, -7, 9)
func1(values)
func1(*values)


# 2. Variable keyword arguments **로 key value params를 전달 가능
def func2(**kwargs):
    print(kwargs)
func2(a=1, b=42)
func2(**{'a': 1, 'b': 42})
func2(**dict(a=1, b=42))


# 3. Keyword only arguments
# variable positional arguments 뒤에 오는 변수나 bare * 뒤의 변수는 keyword only args.
def kwo1(*a, c):
    print(a, c)
kwo1(1, 2, 3, c=4)
kwo1(c=11)

# kwo1(1, 2) missing 1 required keyword-only argument: 'c'
def kwo2(a, b=42, *, c):
    print(a, b, c)
kwo2(1, b=2, c=3)
kwo2(1, c=5)
# kwo2(1, 2, 3) takes from 1 to 2 positional arguments but 3 were given
# kwo2(1, 2) missing 1 required keyword-only argument: 'c'


# 4. Combining input parameters 여러개를 섞어서 사용할 수 있다.
def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)
# 아래와 같은 방식으로 사용할 수 있다.
func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')


# 5. function 의 default 를 세팅할 땐 mutable value를 피하도록 한다.
# list 나 dictionary 로 default 를 설정하면 함수를 호출할 때 마다
# 기존 list 나 dictionary 에 append 할 때 기존 값이 남는 오류가 발생 할 수 있기 때문이다.
# 따라서 아래와 같이 매번 초기화 해줄 수 있도록 코드를 짜는 것이 좋다.
def func(a=None):
    if a is None:
        a = []


# 6. lambda 함수
def is_multiple_of_five(n):
    return not n % 5
def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))
print(get_multiples_of_five(50))

# is_multiple_of_five와 동일한 역할을 하는 함수를 lambda로 만들어 사용할 수 있다.
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))
print(get_multiples_of_five(50))


# 7. function documentation 함수의 definition 아래에 """{Document}"""와 같은 방식으로 진행한다.
def connect(host, port, user, password):
    """Connect to a database.
    Connect to a PostgreSQL database directly, using the given parameters.
    :param host: The host IP.
    :param port: The desired port.
    :param user: The connection username.
    :param password: The connection password.
    :return: The connection object.    """
    connection = {"host": host, "port": port, "user": user, "password": password}
    return connection
