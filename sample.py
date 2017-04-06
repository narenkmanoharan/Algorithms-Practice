from functools import reduce
def main():
	a = [x for x in range(0,10)]
	result = reduce(lambda x, y : x+y, a)
	print("Sum = {}".format(result))

if __name__ == '__main__':
	main()
