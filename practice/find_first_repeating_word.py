def find_first_repeating_word(s):
	d = {}
	for ch in s.split():
	    if ch in d:
	        print ch, " is already in ", d
	        return
	    else:
	        d[ch] = ""
	print "There is no any repeating word in string"

find_first_repeating_word('rishi is good as rishi does good')
find_first_repeating_word('hem is good as he does good')
find_first_repeating_word('great opprtunity')



 
