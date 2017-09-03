def sort_zeroes_and_ones_in_one_traverse(arr):
	if len(arr) == 1:
		return arr

	pos_of_1st_1 = 1
	i = 0
	while i < len(arr) - 1:
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], a[i]
			pos_of_1st_1 = i + 1
		i += 1	

res = sort_zeroes_and_ones_in_one_traverse([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0])
print res