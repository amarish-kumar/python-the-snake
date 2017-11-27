"""
	{
		"dateOfCreation": "27 Nov 2017",
		"aim": "Using collections.Counter in Python2",
		"pythonVersion": "2.7.13",
		"codedBy": "Rishikesh Agrawani"
	}
"""

from collections import Counter

evens = [54, 2, 0, 54, 72, 56, 54, 2,54, 98, 0, -12, 0, 54]
odds = (1, 3, -7, 3, 1, 5, 9, 17, 1, 3)
details = {"A": 25, "B": 3, "C": -1 }

# 3 ways to initialize
# 1) With sequence of items
print Counter(evens)
print Counter(odds)

# 2) With dictionary containing keys and counts
print Counter(details)

# 3) With keyword arguments mapping string names to counts
print Counter(Z=4, RISHI=5, HEM_3=6, MALINI2=9)

