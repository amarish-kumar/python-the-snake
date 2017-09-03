"""
	{
		"created_on": "28 Aug 2017",
		"aim": "Calculating the absoulte difference of sum of diagonals of an square matrix",
		"coded_by": "Rishikesh Agrawani"
	}
"""

# Defining matrix of size 4x4
matrix = [
			[1, 2, 3, 9],
			[7, 9, 4, 7],
			[5, 7, 8, 6],
			[8, 6, 2, 3]
		]

# Calculating number of rows/columns
l = len(matrix)

# Getting all elements of primary diagonal in an array
primary_diagonal = [matrix[i][i] for i in range(l)] 

# Getting all elements of secondary diagonal in an array
secondary_diagonal = [matrix[i][l-1-i] for i in range(l)] 

# Printing lists containing diagonal elements
print primary_diagonal		# [1, 9, 8, 3] => sum = 21
print secondary_diagonal	# [9, 4, 7, 8] => sum = 28 => finally abs_diff will be 7

# Calculating differece of corresponding elements of lists 
# and storing final result in new array
arr = map(lambda t: t[0]-t[1], zip(primary_diagonal, secondary_diagonal))

print arr # [-8, 5, 1, -5]

# Printing final desired result i.e. the absoulte difference of sum of diagonals
print abs(sum(arr)) # abs(-7) = 7

