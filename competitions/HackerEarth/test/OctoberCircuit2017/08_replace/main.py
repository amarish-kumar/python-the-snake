"""
    {
        "dateOfCreation": "29 Oct 2017",
        "codedBy": "Rishikesh Agrawani"
    }
"""

from sys import stdin, stdout

arr_size, queries = map(int, stdin.readline().split())
arr = map(int, stdin.readline().split())
i = 0 
while i < queries:
    query = map(int, stdin.readline().split())
    if query[0] == 1:
        for j in xrange(query[1]-1, query[2]):
            if arr[j] == query[3]:
                arr[j] = query[4]
    else:
        stdout.write(str(arr[query[1]-1: query[2]].count(query[3]))+"\n")
        # print str(arr[query[1]-1: query[2]].count(query[3]))
    i += 1