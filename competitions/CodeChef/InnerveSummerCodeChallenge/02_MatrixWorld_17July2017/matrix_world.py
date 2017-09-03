# A function that computes the exact location
# for all test cases

def get_exact_position():
	testcases = int(raw_input().strip()) + 1

	testcase = 1

	while testcase < testcases:
		steps = int(raw_input().strip())

		step = 1
		x, y = 0, 0

		while step <= steps:
			if (step % 2) != 0:	#move 1 step towards x-direction
				x += 1
			else: #move 2 steps towards y-direction
				y += 2
			step += 1

		print "%d %d" % (x, y)
		testcase += 1

if __name__ == "__main__":
	get_exact_position()
