# 11 June 2015

# gcd number
def gcd(a,b):
	return abs(a) if b==0 else gcd(b, a%b)

def gcdof(*args):
	return reduce(gcd, args)

g1 = gcdof(1, 2, 10)
g2 = gcdof(4, 12, 16)
g3 = gcdof(16, 4, 12)
g4 = gcdof(12, 16, 4)

print g1, g2, g3, g4	# 1 4 4 4

# nth fibonacii fibonacii number
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def fibonacii(n):
	if n==1 or n==2:
		return 1
	return fibonacii(n-1) + fibonacii(n-2)

f1 = fibonacii(1)
f2 = fibonacii(2)
f3 = fibonacii(3)
f10 = fibonacii(10)

print f1, f2, f3, f10	# 1 1 2 55




