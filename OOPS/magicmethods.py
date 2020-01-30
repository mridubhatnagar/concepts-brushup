"""
Learning Magic Methods.
1. __repr__ - used for purpose of debugging, logging. Developer readable.
2. __str__ - more focused towards display and end user.
3. If both are used together. Output of str gets returned.
4. On background __repr__(), __str__() get executed.
5. __add__ - adds two objects together. On calling emp1 + emp2 returns added pay value.
6. __len__ - if we want length to work on objects.

"""

class Employee:

	raise_amount=1.04


	def __init__(self, first, last, pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay=int(self.pay * self.raise_amount)


	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


	def __str__(self):
		return '{} {}'.format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())


emp_1 = Employee('Mridu', 'Bhatnagar', 50000)
emp_2 = Employee('Shlok', 'Bhatnagar', 60000)
print(emp_1 + emp_2)

print(len(emp_1))
