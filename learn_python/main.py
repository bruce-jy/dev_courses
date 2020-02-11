# 2020.02.11
# Iterating (73~100)

surnames = ['James', 'John', 'Michael', 'Jenny']
ages = [20, 30, 40, 50]
nationalities = ['UK', 'USA', 'Spain', 'France']

# 1. enumerate()
# iterable의 길이만큼 돌면서 iterable의 value를 iterate 값으로 받아올 수 있음
# 첫번째 변수로 index, 두번째로 iterable의 value. enumerate(iterables, start position)
for position, surname in enumerate(surnames, 4):
    print(position, surname)

# 2. zip()
# zip은 여러 iterable를 tuple로 iterating
for surname, age, nationality in zip(surnames, ages, nationalities):
    print(surname, age, nationality)
# tuple 타입으로 받을 수 있음
for data in zip(surnames, ages, nationalities):
    print(type(data))
    break

# 3. count() from itertools
# count(start, by)로 무한 반복
from itertools import count
for n in count(5, 3):
    if n > 20:
        break
    print(n)

# 4. compress() from itertools
# iterable에서 값을 추출 한다.
from itertools import compress
data = range(10)
even_selector = [1, 0] * 10 # == [True, False]
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

# 5. permutaions() from itertools
# Permutation을 찾는다
from itertools import permutations
print(list(permutations('ABC')))