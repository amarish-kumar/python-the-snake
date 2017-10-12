# Goldman Sachs
# I told I am not familiar in Java so he told me to conduct interview later.
# Just after that I coded it. 

def find_first_non_repeating_char(s):
	for ch in s:
		if s.count(ch) > 1:
			continue
		else:
			return ch
	return -1

testcases = int(input().strip())
i = 0
while i < testcases:
    int(input().strip()) # I am not using this value
    print (find_first_non_repeating_char(input().strip()))
    i += 1
