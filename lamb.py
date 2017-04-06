from functools import reduce
mul = list(reduce(lambda x: x**3,[1,2,3]))
for x in mul:
	print(x)
