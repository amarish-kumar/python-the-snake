# A function that does primality test
def is_prime(n):
	# print "Test", n
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
		# print l2
		l.append(l2)
		# print "IN,", l
		i = i + 1
	# print "OUT,", l

	i = 0
	while i < n:
		j = 0
		while j < n:
			total = 0

			if not i - 1 < 0:
				total += l[i - 1][j]

			print l[i-1][j]
			
			print "1=>", total

			try:
				total += l[i + 1][j]
			except:
				print "Error2"
				total += 0

			print "2=>", total

			if not i -1 < 0:
				total += l[i][j - 1]
			

			print "3=>", total

			try:
				total += l[i][j + 1]
			except:
				print "Error4"
				total += 0	

			print "4=>", total
			
			if is_prime(total):
				prime_cells += 1

			j += 1
		i += 1

	return prime_cells

def is_prime_messages():
	print "1,", is_prime(1)
	print "-1,", is_prime(-1)
	print "2,", is_prime(2)
	print "3,", is_prime(3)
	print "11,", is_prime(11)
	print "7,", is_prime(7)
	print "17,", is_prime(17)
	print "34,", is_prime(34)
	print "27,", is_prime(27)
	print "117,", is_prime(117)
	print "12,", is_prime(12)
	print "53,", is_prime(53)

if __name__ == "__main__":
	# is_prime_messages()
	print get_the_prime_cells()


# 2
# 1 2 
# 3 4
# 4

(5, 5) => 2
(5, 5) => 2

# 4
# 1 2 3 4
# 5 6 7 8
# 2 3 4 5
# 9 5 4 3
# 8

(7, 10, 13, 11)	=> 3
(9, 17, 21, 16) => 1
(17, 17, 19, 15) => 3
(7, 16, 12, 9) => 1
	