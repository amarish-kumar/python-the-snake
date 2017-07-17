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
	no_of_items, queries = [int(n) for n in raw_input().strip().split()]

	print no_of_items, type(no_of_items)
	print queries, type(queries)

	arr = [int(n) for n in raw_input().strip().split()]
	print arr, type(arr)

	# queries
	for i in range(queries):
		# 1 <= l <= r <= n-2
		print "Input again(l, r)"
		l, r =  [int(n) for n in raw_input().strip().split()]
		print "L",l,"R",r
		print arr[l-1:r]
		farr = []
		for item in arr[l-1:r]:
			farr.append(fibonacii(item))
		print "FiboArr", farr
		print "Finally",gcdof(farr)%(10**9) + 7

main()

# MacBook-Pro:test admin$ python input_test2.py 
# 3 2
# 3 <type 'int'>
# 2 <type 'int'>
# 2 4 8
# [2, 4, 8] <type 'list'>
# Input again(l, r)
# 1 3
# L 1 R 3
# [2, 4, 8]
# FiboArr [1, 3, 21]
# Finally 8
# Input again(l, r)
# 2 3
# L 2 R 3
# [4, 8]
# FiboArr [3, 21]
# Finally 10


