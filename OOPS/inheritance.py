"""
Inheritance

1. Allows us to access variables and methods from parent class.
2. Developer class inherits parent class employee.
3. Checks for __init__ in developer class first.
4. If inherited class needs to be initialized with some more variables. Add __init__ to the 
inherited class. Ex- In Developer class. Add programming language as parameter.
5. To initialize parent class variables from child class. Use super().__init__(first, last, pay)

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


class Developer(Employee):
	raise_amount=1.05

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang=prog_lang


class Manager(Employee):
	raise_amount=1.05

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees=[]
		else:
			self.employees = employees


	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)


dev_1=Developer('Mridu', 'Bhatnagar', 50000, 'Python')
dev_2=Developer('Mridu', 'Bhatnagar', 60000, 'Go')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Abc', 'XYZ', 80000, [dev_1])
print(mgr_1.email)
print(mgr_1.employees)