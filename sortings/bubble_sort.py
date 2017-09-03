def bubble_sort(arr):
	n = len(arr)
	i = n-2
	while i >= 0:
		j = 0
		swapped = False
		while j <= i:
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = a[j+1], a[j]
				swapped = True
			j += 1
		if not swapped:
			break
		i -= 1

a = [1, 5, -1, 6, 78, 34, 4, 2, -4, 9]
print a
bubble_sort(a)
print a
