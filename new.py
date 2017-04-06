a = 'Miffy\'s breakfast'
b = ''
size = len(a)
for x in range(size):
	index = -(x) -1
	print(a[index])
	b += a[index]
print(b)
