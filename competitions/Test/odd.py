def  oddNumbers(l, r):
	if l%2 == 0:
		l = l + 1

	odds = []
	while l <= r:
		odds.append(l)
		l = l + 2
		
	return odds
		

print oddNumbers(2, 5)
print oddNumbers(3,10)