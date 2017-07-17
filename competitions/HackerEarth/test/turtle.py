def is_prime(n):
	if n<=1:
		return False;
 
	#Check from 2 to n-1
	for i in xrange(2, n):
		if n%i == 0:
			return False;
		return True

def main():
    # n rows, m columns
    n, m = [int(n) for n in raw_input().strip().split()]
    
    matrix = []
    graph = []
    for i in xrange(n):
        arr = [int(n) for n in raw_input().strip().split()]
        matrix.append(arr) 
        
        temp_arr = []
        for item in arr:
            if is_prime(item):
                temp_arr.append(1) 
            else:
                temp_arr.append(0)
        graph.append(temp_arr)

    print matrix
    print graph

# Starter 
main()
    
