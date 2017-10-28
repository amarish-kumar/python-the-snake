"""
    {
        "dateOfCreation": "29 Oct 2017",
        "codedBy": "Rishikesh Agrawani"
    }
"""

from sys import stdin, stdout

n = int(stdin.readline())
strengths1 = [int(num) for num in stdin.readline().split()]  

m = int(stdin.readline())
strengths2 = [int(num) for num in stdin.readline().split()]  

max_strength = max(strengths2)
max_inc = max_strength + 1
amount = 0
for strength in strengths1:
    if max_inc > strength:
        amount += (max_inc - strength)
        
stdout.write(str(amount))


# """
#     {
#         "dateOfCreation": "29 Oct 2017",
#         "codedBy": "Rishikesh Agrawani"
#     }
# """

# n = int(raw_input().strip())
# strengths1 = [int(num) for num in raw_input().strip().split()]  

# m = int(raw_input().strip())
# strengths2 = [int(num) for num in raw_input().strip().split()]  

# max_strength = max(strengths2)
# max_inc = max_strength + 1
# amount = 0
# for strength in strengths1:
#     if max_inc > strength:
#         amount += (max_inc - strength)
        
# print amount

# """
#     {
#         "dateOfCreation": "29 Oct 2017",
#         "codedBy": "Rishikesh Agrawani"
#     }
# """

# n = int(raw_input().strip())
# strengths1 = [int(num) for num in raw_input().strip().split()]  

# int(raw_input().strip())
# strengths2 = [int(num) for num in raw_input().strip().split()]  

# max_strength = max(strengths2)
# # max_inc = max_strength + 1
# amount = 0
# i = 0
# while i < n:
#     if max_strength + 1 > strengths1[i]:
#         amount += (max_strength + 1 - strengths1[i])
#     i += 1
        
# print amount


