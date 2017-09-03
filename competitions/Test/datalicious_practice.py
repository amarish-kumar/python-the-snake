def  maxDifference(a):
	# l = []	
	# for i in range(len(a)):
	# 	for j in range(i+1, len(a)):
	# 		l.append((a[i],a[j]))

	# print l

	# print "Again"
	# l = []	
	# i = 0
	# while i < len(a):
	# 	j = i + 1
	# 	while j < len(a):
	# 		l.append((a[i],a[j]))
	# 		j = j + 1
	# 	i = i + 1

	# print l

	max_diff = 0
	exists = False
	i = 0
	while i < len(a):
		j = i + 1
		while j < len(a):
			diff = a[i] - a[j]
			if diff != 0:
				exists = True
				if diff > max_diff:
					max_diff = diff
			j = j + 1
		i = i + 1

	if exists:
		return max_diff
		
maxDifference([1, 2, 3, 5, 6])