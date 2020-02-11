# 2020.02.11
# Comprehension (142~147)

# comprehension
print([n for n in range(10)])

# nested comprehension
print([(a, b) for a in range(4) for b in range(4)])

# filtering a comprehension 피타고라스 정리
from math import sqrt
pt_tri = [(a, b, sqrt(a**2 + b**2)) for a in range(1, 10) for b in range(a, 10)]
print(list(filter(lambda triple: triple[2].is_integer(), pt_tri)))

# dict comprehension
from string import ascii_lowercase
print(dict((c, k) for k, c in enumerate(ascii_lowercase, 1)))

# set comprehension
word = 'Hello'
print(set(c for c in word))
print({c for c in word})
