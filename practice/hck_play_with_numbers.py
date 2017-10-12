# n, q = (int(s) for s in raw_input().strip().split())
# arr = [int(s) for s in raw_input().strip().split()]
import sys
n, q = map(int, sys.stdin.readline().split(' '))
arr = map(int, sys.stdin.readline().split(' '))
i = 0
while i < q:
    l, r = map(int, sys.stdin.readline().split(' '))
    sub_arr = arr[l-1:r]
    print sum(sub_arr)/len(sub_arr)
    i += 1