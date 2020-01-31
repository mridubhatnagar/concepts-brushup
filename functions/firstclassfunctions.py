"""
Learning
1. Function can be passed as argument.
2. Returned from a function.
3. assigned to a variable.
"""

def square(x):
	return x*x

#Passing function as argument
def my_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result


squares=my_map(square, [1,2,3,4,5])
print(squares)


def cube(x):
	return x*x*x


def logger(msg):
	def log_message():
		print('Log: ', msg)

	return log_message

f=logger('Hi')
f()
