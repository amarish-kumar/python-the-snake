# 11 June 2015
no_of_items, queries = [int(n) for n in raw_input().strip().split()]

print no_of_items, type(no_of_items)
print queries, type(queries)

arr = [int(n) for n in raw_input().strip().split()]
print arr, type(arr)

# l, r =  [int(n) for n in raw_input().strip().split()]
# print l, type(l)
# print r, type(r)

# queries
for i in range(queries):
	# 1 <= l <= r <= n-2
	l, r =  [int(n) for n in raw_input().strip().split()]