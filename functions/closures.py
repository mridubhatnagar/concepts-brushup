"""
Learning

1. Inner function has access to free variable message which is present in 
local scope of outer_function.
2. Remembers message variable even after outer function has finished executing.
"""


def outer_function(msg):
	message=msg

	def inner_function():
		print(message)
	return inner_function

hi_func = outer_function('Hi')
hi_func()
bye_func = outer_function('Bye')
bye_func()