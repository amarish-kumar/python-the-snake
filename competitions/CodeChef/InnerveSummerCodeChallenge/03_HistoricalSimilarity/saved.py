def get_list_with_unique_elements(s):
	l = []
	while s:
		if s[0] not in l:
			l.append(s[0])
			s = s.replace(s[0], "")

	return l

def check_historical_similarity():
	testcases = int(raw_input().strip()) + 1

	testcase = 1

	while testcase < testcases:
		p, q = (s for s in raw_input().strip().split())
		
		# set_p = get_list_with_unique_elements(p)
		# set_q = get_list_with_unique_elements(q)
		# yes = False
		# print set_p, set_q
		# while set_p:
		# 	p = p.replace(set_p[0], set_q[0])
		# 	if p == q:
		# 		print "YES"
		# 		yes = True
		# 		break

		# 	set_p.remove(set_p[0])
		# 	set_q.remove(set_q[0])

		# if not yes:
		# 	print "NO"
		# testcase += 1
		while p and q:
			p = p.replace(p[0], "")
			q = q.replace(q[0], "")

		if p == "" and q == "":
			print "YES"
		else:
			print "NO"

		testcase += 1

if __name__ == "__main__":
	check_historical_similarity()
