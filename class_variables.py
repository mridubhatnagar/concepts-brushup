"""
Learnings

1. Class variables  
    - value of a variable common to a class

2. Class methods
    - accepts cls as the first argument
    - helps in creating a instance of a class
    - ex datetime module examples, from_string example

3. Static methods
    - neither access a class variable nor a instable variable as argument.
    - ex. check age, check weekend, weekday etc.

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

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount=amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)




emp_1=Employee('Mridu', 'Bhatnagar', 15000)
emp_2=Employee('Mridu', 'Bhatnagar', 12000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amount)
Employee.set_raise_amount(1.05)
print(emp_1.raise_amount)


emp_str_1='Joe-Doe-70000'
emp_str_2='Steve-SMith-30000'
emp_str_3='Joe-Doe-90000'


first, last, pay = emp_str_1.split('-')
emp_1 = Employee(first, last, pay)

print(emp_1.email)
print(emp_1.pay)

new_emp_1=Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)



