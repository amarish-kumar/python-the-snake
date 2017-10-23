"""
	{
		"aimOfScript": "To check if a given list is pairwise sorted or not",
		"sourceUrl": "http://www.geeksforgeeks.org/check-given-array-pairwise-sorted-not/",
		"purpose": "Error fix, Python implementaion of C++",
		"codedOn": "22 Oct 2017, Sun",
		"codedBy": "Rishikesh Agrawani"
	}
"""


def checkPairWiseSorted(arr):
	"""
	Block of code that calls returns True if list(array) is pairwise sorted otherwise False
	"""

	for index in xrange(0, len(arr), 2):
		try:
			if arr[index] > arr[index + 1]:
				return False
		except IndexError:	# In case of odd number of elements in the list
			return True

	return True


def main(arrs):
	"""
	Block of code that calls checkPairWiseSorted() to look whether an list(array) is pairwise sorted or not
	"""
	for arr in arrs:
		if checkPairWiseSorted(arr):
			print "Yes"
		else:
			print "No"

# Starting point 
if __name__ == "__main__":
	arr1 = [10, 15, 9, 9, 1, 5]
	arr2 = [10, 15, 8, 9, 10, 5]
	arr3 = [2, 5, 3, 7, 9, 11, 12]
	arr4 = []
	arr5 = [12]

	main([arr1, arr2, arr3, arr4, arr5])


"""
Yes
No
Yes
Yes
Yes
"""
