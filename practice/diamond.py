# 0 	1 	2 	3 	4 	5 	6 	7 	8 	

# 1 	2 	3 	4 	5 	6 	7 	8 	9 	

# 2 	3 	4 	5 	6 	7 	8 	9 	10 	

# 3 	4 	5 	6 	7 	8 	9 	10 	11 	

# 4 	5 	6 	7 	8 	9 	10 	11 	12 	

# 5 	6 	7 	8 	9 	10 	11 	12 	13 	

# 6 	7 	8 	9 	10 	11 	12 	13 	14 	

# 7 	8 	9 	10 	11 	12 	13 	14 	15 	

# 8 	9 	10 	11 	12 	13 	14 	15 	16

c = 1
four, four2 = 7, 7
for i in range(four2*2 + 1):		#rows
	for j in range(four2*2 +1):	#columns
		if i <= four2:
			if i+j == four2:
				j = i+j		# we can use another variable too, but this is a way of saving memory
				for k in range(c):
					print j,"\t",
					j += 1

				if i == four2:
					four += 2
					c -= 2
					pass
				else:
					c += 2

				break
			else:
				print "\t",
		else:
			if i + j == four:
				j = four	# we can use another variable too, but this is a way of saving memory
				for k in range(c):
					print j,"\t",
					j += 1
				c -= 2
				four += 2
				break
			else:
				print "\t",
	print "\n"
	


"""
c = 1
for i in range(9):	#rows
	for j in range(9):	#columns
		if i+j == 4:
			j = i+j	# we can use another variable too, but this is a way of saving memory
			for k in range(c):
				print j,"\t",
				j += 1
			break
		else:
			print "\t",
	print "\n"
	c += 2
"""

"""
c = 1
for i in range(9):	#rows
	for j in range(9):	#columns
		if i+j == 4:
			# j = i+j	# we can use another variable too, but this is a way of saving memory
			for k in range(i+j, i+j+c):
				print k,"\t",
				# j += 1
			break
		else:
			print "\t",
	print "\n"
	c += 2
"""
