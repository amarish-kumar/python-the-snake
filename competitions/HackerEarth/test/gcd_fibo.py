# 11 June 2015

def gcd(a,b):
	return abs(a) if b==0 else gcd(b, a%b)

def gcdof(arr):
	return reduce(gcd, arr)

def fibonacii(n):
	if n==1 or n==2:
		return 1
	return fibonacii(n-1) + fibonacii(n-2)


def main():
	# N and Q (1 <= N <= 10^5, 1 <= Q <= 10^5)
	no_of_items, queries = [int(n) for n in raw_input().strip().split()]

	# A1 A2 A3 ... AN (1 <= Ai <= 10^9)
	arr = [int(n) for n in raw_input().strip().split()]

	# queries
	for i in range(queries):
		l, r =  [int(n) for n in raw_input().strip().split()]

		farr = []
		for item in arr[l-1:r]:
			farr.append(fibonacii(item))

		gcd = gcdof(farr)
		if gcd >= 10**9: 
			print gcd%(10**9) + 7
		else:
			print gcd

main()

# MacBook-Pro:test admin$ python gcd_fibo.py 
# 3 2
# 2 4 8
# 1 3
# 1
# 2 3
# 3

