"""
	{
		"solved_on": "6 Aug 2017",
		"link": "https://www.hackerearth.com/challenge/hiring/payu-backend-developer-hiring-challenge/problems/c0ac9fb5483546798b02028466add473/",
		"code_by": "Rishikesh Agrawani",
		"submission_status": "Successful, gained 100 marks"
	}
"""

# A function that destroys the balls and prints the relevant message to user
def destroy_balls():
    t = int(raw_input())
    i = 0 
    while i < t:
        n = int(raw_input())
        arr = [int(num) for num in raw_input().split()]
        while arr:
        	element = len(arr) # Getting number of elements
        	found = False
        	while element in arr: # Remove all the elements will same current color
        		found = True
        		arr.remove(element)
        	if found: # If current color is not in the list/arr 
        		continue
        	else:
        		break
        if arr:
        	print "NO"
        else:
        	print "YES"
        i += 1 

# Call function to destroy balls 
destroy_balls()

"""
	{
		"solved_on": "6 Aug 2017",
		"link": "https://www.hackerearth.com/challenge/hiring/payu-backend-developer-hiring-challenge/problems/c0ac9fb5483546798b02028466add473/",
		"code_by": "Rishikesh Agrawani",
		"submission_status": "Successful, gained 100 marks"
	}
"""

# t = int(raw_input())
# i = 0 
# while i < t:
#     n = int(raw_input())
#     arr = [int(num) for num in raw_input().split()]
#     while arr:
#     	element = len(arr)
#     	found = False
#     	while element in arr:
#     		found = True
#     		arr.remove(element)
#     	if found:
#     		continue
#     	else:
#     		break
#     if arr:
#     	print "NO"
#     else:
#     	print "YES"
#     i += 1 

    