# link: https://www.hackerearth.com/challenge/test/programming-practice-challenge/algorithm/little-shino-and-common-factors/submission/10464959/
# 6 Aug 2017
# 64 marks

# define gcd function
# def gcd(x, y):
#   """
#     This function implements the Euclidian algorithm
#     to find G.C.D. of two numbers
#   """
#   while(y):
#    	x, y = y, x%y

#   return x

# a, b = (int(num) for num in raw_input().split())
# common_factors = 1	# 1 is divisor of all numbers 
# gcd_number = gcd(a, b)

# if gcd_number != 1:
# 	common_factors += 1

# i = 2
# while i < gcd_number:
# 	if (a % i) == 0 and (b % i == 0):
# 		common_factor	s += 1
# 	i += 1

# print common_factors


# OPT
# A function that returns gcd of a & b
# def gcd(x, y):
#   """
#     This function implements the Euclidian algorithm
#     to find G.C.D. of two numbers
#   """
#   while(y):
#    	x, y = y, x%y

#   return x

# # Starting point
# a, b = (int(num) for num in raw_input().split())
# common_factors = 1	# 1 is divisor of all numbers 
# gcd_number = gcd(a, b)

# if gcd_number != 1:
# 	common_factors += 1

# i = 2
# g = gcd_number//2
# while i <= g:
# 	if (a % i) == 0 and (b % i == 0):
# 		common_factors += 1
# 	i += 1

# print common_factors




# GOT 68, partially solved
# A function that returns gcd of a & b
# def gcd(x, y):
#   """
#     This function implements the Euclidian algorithm
#     to find gcd(hcf) of two numbers
#   """
#   while(y):
#     x, y = y, x%y

#   return x

# # Starting point
# a, b = (int(num) for num in raw_input().split())
# common_factors = 1  # 1 is divisor of all numbers 
# gcd_number = gcd(a, b)

# if gcd_number != 1:
#   common_factors += 1

# i = 2
# g = gcd_number//2
# while i <= g:
#   if (a % i) == 0 and (b % i == 0):
#     common_factors += 1
#   g = g//2
#   i += 1

# print common_factors


# A function that returns gcd of a & b
def gcd(x, y):
  """
    This function implements the Euclidian algorithm
    to find gcd(hcf) of two numbers
  """
  while(y):
    x, y = y, x%y

  return x

# Starting point
a, b = (int(num) for num in raw_input().split())
common_factors = 1  # 1 is divisor of all numbers 
gcd_number = gcd(a, b)

if gcd_number != 1:
  common_factors += 1

i = 2
g = int(pow(gcd_number, 1//2.0))
while i <= g:
  if n%i==0:
    if (n/i == i)
      common_factors += 1;
    else
      common_factors += 2;
  i += 1

print common_factors


int commDiv(int a,int b)
{
    // find gcd of a,b
    int n = gcd(a, b);
 
    // Count divisors of n.
    int result = 0;
    for (int i=1; i<=sqrt(n); i++)
    {
        // if 'i' is factor of n
        if (n%i==0)
        {
            // check if divisors are equal
            if (n/i == i)
                result += 1;
            else
                result += 2;
        }
    }
    return result;
}


