# Complete the function below.

# def  maxDifference(a):
    
"""
	{
		"Date of test": 2 July 2017,
		"Aim": "To print of max difference in pairs"
		"Coded by": "Rishikesh Agrawani"
	}
"""

def  maxDifference(a):
	max_diff = 0
	exists = False
    
	i = 0
	while i < len(a):
		j = i + 1
		while j < len(a):
			diff = a[i] - a[j]
			if diff < 0:
				exists = True
				if abs(diff) > max_diff:
					max_diff = abs(diff)
			j = j + 1
		i = i + 1

	if exists:
		return max_diff

	return -1

print maxDifference([2, 3, 10, 2, 4, 8, 1])