"""
Learning Decorators

1. Function that takes another function as an argument. Adds some kind of functionality.
Returns another function. All of this without altering the source code of outer function.

2. Can be used for class as well as function.
"""


def decorator_function(orignal_function):
	def wrapper_function(*args, **kwargs):
		print('Wrapper executed!')
		return orignal_function(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print('display function ran')


@decorator_function
def display_info(name, age):
	print('display info ran with arguments {} {}'.format(name, age))


#decorated_display = decorator_function(display)
#decorated_display()

display()
display_info('abc', 10)