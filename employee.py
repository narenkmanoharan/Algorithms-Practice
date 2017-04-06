import datetime

class employee:

	raise_pay = 1.05

	def __init__(self, last, first, id, pay):
		self.last = last
		self.first = first
		self.id = id
		self.pay = pay

	def fullname(self):
		return '{}, {}'.format(self.last, self.first)

	def email(self):
		return self.first + '.' + self.last + '@gmail.com'

	def monthly_salary(self):
		return round(self.pay/12,2)

	def promotion(self):
		return self.pay * self.raise_pay

	@classmethod
	def fromstring(cls, emp):
		first, last, id, pay = emp.split(' ')
		return cls(last, first, id, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday == 6:
			return False
		return True


def main():
	naren = employee('Manoharan', 'Narendra Kumar', 1001237691, 500000)
	miffy_date = datetime.date(2016, 12, 1)
	val = employee.is_workday(miffy_date)
	if val == True:
		print("Miffy's going to work today :(")
	else:
		print("Miffy's not going to work today :D :D")

if __name__ == '__main__':
	main()
