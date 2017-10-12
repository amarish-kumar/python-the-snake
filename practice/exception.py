"""
	{
		"created_on": "12 Oct 2017",
		"aim": "To understand the exception handling concept in Python",
		"created_by": "Rishikesh Agrawani",
		"python_ver": "3.6.2"
	}
"""

# Example 1 
print("\nExample 1")
try:
	a, b = 12, 0
	c = a / b
except ZeroDivisionError:
	print("You tried to divide number by 0")	

# Example 2
print("\nExample 2")
try:
	d = int(input("Enter a integer number: "))
except ValueError:
	print("You entered an invalid integer")

# Example 3
print("\nExample 3")
def trial_examples(a, b):
	try:
		c = a / b
		d = int(input("Enter a integer number: "))
	except ZeroDivisionError:
		print("You tried to divide number by 0")
	except ValueError:
		print("You entered an invalid integer")

for a, b in [(12, 0),(12, 15)]:
	trial_examples(a,b)

# Example 4
print("\nExample 4")
def trial_examples(a, b):
	try:
		c = a / b
		d = int(input("Enter a integer number: "))
	except (ZeroDivisionError, ValueError)	:
		print("Either Division by 0 or invalid integer has been entered")

for a, b in [(13, 0), (-1, 5)]:
	trial_examples(a,b)

"""
MacBook-Pro-2:practice admin$ python3 exception.py 

Example 1
You tried to divide number by 0

Example 2
Enter a integer number: pyth 
You entered an invalid integer

Example 3
You tried to divide number by 0
Enter a integer number: tig
You entered an invalid integer

Example 4
Either Division by 0 or invalid integer has been entered
Enter a integer number: 12
"""
