    # define gcd function
    def gcd(x, y):
      """
        This function implements the Euclidian algorithm
        to find G.C.D. of two numbers
      """
      while(y):
       	x, y = y, x%y

      return x

    # define lcm function
    def lcm(x, y):
      """
        This function takes two
        integers and returns the L.C.M.
        """
      lcm = (x*y)//gcd(x,y)
      return lcm

    def nochange_bits(input1,input2,input3):
    	length = len(input1)

    	if (input2 < 0 ) or (input2 > length) or (input3 < 0) or (input3 > length):
    		return -1

    	reps = length/input2
    	reps2 = length/input3

    	lcm_number = lcm(input2, input3)

    	count = length//lcm_number
    	return length - (reps + reps2 - 2*count ) 
	
try:
  ip1 = raw_input()
except:
  ip1 = None

ip2 = int(raw_input());
ip3 = int(raw_input());

output = nochange_bits(ip1,ip2,ip3)

print(str(output))
