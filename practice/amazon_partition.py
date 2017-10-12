def get_subsets(arr):
	set1 = []
	set2 = []
	arr.sort()
	while arr:
		if sum(set1) == sum(set2):
			set1.append(arr.pop(0))
			if len(arr) > 0:
				set2.append(arr.pop(len(arr)-1))
		elif sum(set1) < sum(set2):
			set1.append(arr.pop(0))
		else:
			set2.append(arr.pop(0))
	return set1, set2


def get_absolute_diff(arr):
	sub_set = get_subsets(arr)
	print sub_set
	return abs(sum(sub_set[0]) - sum(sub_set[1]))


if __name__ == "__main__":
	arr = [1, 11, 6, 5]
	print get_absolute_diff(arr)

	arr = [1, 11, 6, 5, 4, 12, 11]
	print get_absolute_diff(arr)

	arr = [3, 1, 4, 2, 2, 1]
	print get_absolute_diff(arr)

	arr = [5, 3, 2, -5, 6, -6, 45]
	print get_absolute_diff(arr)