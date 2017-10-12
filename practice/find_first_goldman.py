# Goldman Sachs
# I told I am not familiar in Java so he told me to conduct interview later.
# Just after that I coded it and checked in geeksforgeeks, I was right.

def find_first_non_repeating_char(s):
	for ch in s:
		if s.count(ch) > 1:
			continue
		else:
			return ch
	return -1

print find_first_non_repeating_char("geeksforgeeks")
print find_first_non_repeating_char("raghav")
print find_first_non_repeating_char("abac")
print find_first_non_repeating_char("hygull")
print find_first_non_repeating_char("abcabdcbdefg")
print find_first_non_repeating_char("abccba")

# f
# r
# b
# h
# e
# -1