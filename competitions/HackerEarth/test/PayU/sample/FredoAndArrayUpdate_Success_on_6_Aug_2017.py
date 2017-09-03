# link: https://www.hackerearth.com/challenge/test/programming-practice-challenge/algorithm/fredo-and-array-update-15/submission/10465579/

# Taking number of elements
n = int(raw_input())

# Getting list input
arr = [int(num) for num in raw_input().split()]

# Getting total sum of elements of list
total = sum(arr)

# Getting totla number of items in an array/list
length = len(arr)

# Calculating average of all elements
avg = total/length

# Printing output
print avg+1
