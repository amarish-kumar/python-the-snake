"""
	{
		"created_on": "12 Oct 2017",
		"aim": "To understand the try, except and finally blocks",
		"created_by": "Rishikesh Agrawani",
		"python_ver": "3.6.2"
	}
"""

def trial_examples(*data):
	print("Got data as ", data)

	try:
		c = data[0] / data[1]
	except ZeroDivisionError:  # it will excute when error occurred
		print("ZeroDivisionError Exception occurred")
	finally:  # it will always execute 
		print ("You should always try to perform right operations")
		print()

for a,b in [(6, 7), (4, 0)]:
	trial_examples(a, b)

"""
Got data as  (6, 7)
You should always try to perform right operations

Got data as  (4, 0)
ZeroDivisionError Exception occurred
You should always try to perform right operations

"""