a = [x for x in range(100) if x % 5 == 2]
print(a)
res = list(filter(lambda x: x % 2, a))
print(res)
from functools import reduce
_reduce = reduce(lambda x,y: (x + y), a)
print(_reduce)
