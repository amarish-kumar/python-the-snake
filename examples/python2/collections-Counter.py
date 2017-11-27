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


# Using update() method
c1 = Counter()
c2 = Counter(evens)
c1.update(evens)
print c1, c2

c3 = Counter()
c3.update(evens)
c4 = Counter()
c4.update([1, 5, 7, 1, 4, 5, 7, 5])
print c3, c4
c4.update([1, 5, 7])
print c4
