class reverse_iter:
	def __init__(self,n):
		self.i = 0
		self.n = n

	def __iter__(self):
		return self

	def next(self):
		if self.i <= self.n:
			n = self.n
			self.n -= 1
			return n
		else:
			raise StopIteration()

def main():
	x = reverse_iter(2)
	print("Hello Miffy Kutty, Look at this")
	print(x.next())
	print(x.next())
	print(x.next())


if __name__ == '__main__':
	main()
