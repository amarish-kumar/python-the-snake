def check_historical_similarity():
	testcases = int(raw_input().strip()) + 1

	testcase = 1

	while testcase < testcases:
		p, q = (s for s in raw_input().strip().split())
		
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
