"""
	{
		"createdOn": "23 Oct 2017, Tues",
		"aim": "using decortor in Python",
		"pythonVersion": "Python 2.7.13",
		"codedBy": "Rishikesh Agrawani"
	}
"""

def get_squares_upto(num):
	return [n ** 2 for n in range(1, num)]

def get_cubes_upto(num):
	return [n ** 3 for n in range(1, num)]

print (get_cubes_upto(12))

print (get_squares_upto(10))
