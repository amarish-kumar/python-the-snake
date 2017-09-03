"""
	View my submission at

	https://www.hackerearth.com/challenge/competitive/july-circuits-17/algorithm/pythagorean-triangles-0158a4c5/submission/10285529/
	
	<iframe src=https://www.hackerearth.com/submission/key/db59604885114c8b817e8fd64b83851d/?theme=light width='100%' height='1196px' frameborder='0' allowtransparency='true' scrolling='yes'></iframe>
	
	Problem link: https://www.hackerearth.com/challenge/competitive/july-circuits-17/algorithm/pythagorean-triangles-0158a4c5/
"""

# A function that does primality test
def is_prime(n):
	if n <= 1:
		return False

	if n <= 3:
		return True

	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i * i <= n:
		if (n % i) == 0 or n % (i + 2) == 0:
			return False
		i = i + 6 

	return True

def get_the_prime_cells():
	prime_cells = 0
	n = int(raw_input())
	l = []

	i = 0
	while i < n:
		l2 = [int(inp) for inp in raw_input().split()]
		l.append(l2)
		i = i + 1

	i = 0
	while i < n:
		j = 0
		while j < n:
			total = 0

			if not i - 1 < 0:
				total += l[i - 1][j]

			try:
				total += l[i + 1][j]
			except:
				pass

			if not j - 1 < 0:
				total += l[i][j - 1]

			try:
				total += l[i][j + 1]
			except:
				pass	

			if is_prime(total):
				prime_cells += 1

			j += 1
		i += 1

	return prime_cells

# Call get_the_prime_cells() to get all prime numbers
print get_the_prime_cells()
