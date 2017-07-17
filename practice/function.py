def show_params(*args):
	print args
	print type(args)

	for item in args:
		print item

show_params(1, 23.56, 78+67j, [1992, 5, 14])


def show_params(*args):
	print args
	print type(args)

	for item in args:
		print item

show_params(1, 23.56, 78+67j, [1992, 5, 14], (12, 45), {"lang": "Python"})

# Definition of function
def print_message():
	print "Python is an open source programming language."

# Call(Activate) function
print_message()

def cube(n):
	return n**3

def square(n):
	return n*2

print "cube(10) = ", cube(10)
print "square(10) = ", square(10)


def sum(a, b):
	return a+b

print "sum(10,3) = ", sum(10, 3)
print "sum(10,3) + sum(5, 2) = ", sum(10, 3) + sum(5, 2)


def add_all(arr):
	total = 0				# A variable to hold the sum of all numbers in list
	total_items = len(arr)	# Getting the value of total number of items in list
	i = 0

	while i < total_items:
		total += arr[i]
		i += 1
	return total

print "add_all([12, 34, 56, 78, 12, 3]) = ", add_all([12, 34, 56, 78, 12, 3])

