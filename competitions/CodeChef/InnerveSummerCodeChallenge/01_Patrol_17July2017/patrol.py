# A function that computes the time for the given velocities and 
#distance for all testcases

def get_communication_time():
	testcases = int(raw_input().strip()) + 1

	testcase = 1

	while(testcase < testcases):
		u, v, x = (int(num) for num in raw_input().strip().split())
		print "%.10f" % (float(x) / (u + v))
		testcase += 1

if __name__ == "__main__":
	get_communication_time()
