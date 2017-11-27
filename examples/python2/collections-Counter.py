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

# Using subtract()
for i in range(2):
	c4.subtract(c3)
	print c4

c6 = Counter([5, 1, 4, 5, 1, 4, 5])
c7 = Counter((1, 5, 5))
c7.subtract(c6)
print c7


"""
Counter({54: 5, 0: 3, 2: 2, 72: 1, 98: 1, -12: 1, 56: 1})
Counter({1: 3, 3: 3, 5: 1, 9: 1, 17: 1, -7: 1})
Counter({'A': 25, 'B': 3, 'C': -1})
Counter({'MALINI2': 9, 'HEM_3': 6, 'RISHI': 5, 'Z': 4})
Counter({54: 5, 0: 3, 2: 2, 72: 1, 98: 1, -12: 1, 56: 1}) Counter({54: 5, 0: 3, 2: 2, 72: 1, 98: 1, -12: 1, 56: 1})
Counter({54: 5, 0: 3, 2: 2, 72: 1, 98: 1, -12: 1, 56: 1}) Counter({5: 3, 1: 2, 7: 2, 4: 1})
Counter({5: 4, 1: 3, 7: 3, 4: 1})
Counter({5: 4, 1: 3, 7: 3, 4: 1, 72: -1, 98: -1, -12: -1, 56: -1, 2: -2, 0: -3, 54: -5})
Counter({5: 4, 1: 3, 7: 3, 4: 1, 72: -2, 98: -2, -12: -2, 56: -2, 2: -4, 0: -6, 54: -10})
Counter({1: -1, 5: -1, 4: -2})
"""

