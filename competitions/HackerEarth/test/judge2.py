# 11 June 2017
def gcd(a, b):
    return abs(a) if b==0 else gcd(b, a%b) 
    
def gcdof(arr):
    return reduce(gcd, arr) 
    
# def fibonacci(n):
#     if n==1 or n==2:
#         return 1 
#     return fibonacci(n-1) + fibonacci(n-2) 

def get_fibo_seq(r):
    a, b = 0, 1
    arr = []
    for i in 
    
def main():
    # N and Q (1 <= N <= 10^5, 1 <= Q <= 10^5)
    no_of_items, queries =  [int(n) for n in raw_input().strip().split()]
    
    # A1 A2 A3 ... AN (1 <= Ai <= 10^9)
    arr = [int(n) for n in raw_input().strip().split()]
    
    # queries
    for i in xrange(queries):
        l, r = [int(n) for n in raw_input().strip().split()]
        farr = []   #empty list 
        fibonacci = get_fibo_seq(r)
        for item in arr[l-1:r]:
            farr.append(fibonacci[item])
        
        gcd = gcdof(farr)
        if gcd >= 10**9:
            print gcd % (10**9) + 7
        else:
            print gcd

#Starter main() function 
main()

# 3 2
# 2 4 8
# 1 3
# 1
# 2 3
# 3