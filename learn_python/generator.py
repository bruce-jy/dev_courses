# 2020.02.11
# Generator (148~166)

# Classic한 방법
def get_sqrt(n):
    return [x ** 2 for x in range(n)]
print(get_sqrt(4))

# Generator 방식
def get_sqrt_gen(n):
    for x in range(n):
        yield x ** 2
print(list(get_sqrt_gen(4)))
# or
square = get_sqrt_gen(4)
print(next(square))
print(next(square))
print(next(square))
print(square.__next__()) # same as next()

# 응용 방식들
def geo_progression(a, b):
    k = 0
    while True:
        result = a * b**k
        if result < 10**5:
            yield result
        else:
            return
        k += 1

print(list(geo_progression(2, 5)))

# stop 을 통해 generator를 멈추는 방법
stop = False
def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1

c = counter()
print(next(c))
print(next(c))
print(next(c))
stop = True
try:
    print(next(c)) # 더이상 counter가 진행되지 않는다.
except StopIteration:
    print('StopIteration')

# 비슷한 방식으로 특정 text를 send 하여 종료시킬 수 있다
def counter_text(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1

ct = counter_text()
print(next(ct)) # generator가 실행되고 n 은 0으로 초기화된다. -> 0 리턴하고 yield 에서 대기
print(ct.send(('AA'))) # send로 result가 AA가 되고 print reulst 하고 Q가 아니니까 n += 1 후 yield에서 1리턴하고 대기
print(next(ct)) # send 된 것이 없기 때문에 None 이 result 로 print 되고 n += 1 후 yield에서 2리턴하고 대기
try:
    print(ct.send('Q')) # send로 result가 Q가 되고 print result 하고 Q라서 while이 break 되며 generator 종료되며
                        # StopIteration 오류 발생하며 Exception 발생
except StopIteration:
    print('StopIteration')

# yield from
def print_squares():
    for n in range(10):
        yield n ** 2
# 이 코드는
def print_squares_from():
    yield from (n ** 2 for n in range(10))
# 코드와 동일하다.

# generator expression
gens = (k for k in range(10))
print(type([k for k in range(10)]))  # 리스트 생성하는 comprehension
print(type(k for k in range(10)))    # generator
print(list(gens))
print(list(gens))  # 한번 generator 실행되고 나면 값이 날아감

# Generator를 사용해서 코드를 읽기 쉽게 바꿔보는 방법
# 1) sum 하는 경우
def adder(*n):
    return sum(n)
print(sum(map(lambda n: adder(*n), zip(range(100), range(1,101)))))
print(sum(adder(*n) for n in zip(range(100), range(1,101))))

# 2) filter 하는 경우 (부피가 홀수인 값 filter)
cubes = [x ** 3 for x in range(12)]
print(list(filter(lambda x: x % 2, cubes)))
print(list(cube for cube in cubes if cube % 2))

# 3) map filter 하는 경우 (3, 5의 배수인 경우 tuple로 부피 리턴)
print(list(map(lambda n: (n, n**3), filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20)))))
print(list((n, n**3) for n in range(20) if n % 3 == 0 or n % 5 == 0))

# 4) 메모리 효율 및 시간적 측면에서 유리한 방식을 사용해야 한다.
from time import time
curticks = time()
sum([n ** 2 for n in range(10**6)])
print('list comprehension sum timestamp: ', (time() - curticks) * 1000, 'ms')
curticks = time()
sum(n ** 2 for n in range(10**6))
print('generator sum timestamp: ', (time() - curticks) * 1000, 'ms')

curticks = time()
[divmod(a, b) for a in range(1, 4000) for b in range(a, 4000)]
print('list comprehension divmod timestamp: ', (time() - curticks) * 1000, 'ms')
curticks = time()
list(divmod(a, b) for a in range(1, 4000) for b in range(a, 4000))
print('generator divmod timestamp: ', (time() - curticks) * 1000, 'ms')
