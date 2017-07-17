"""
	7353787704  9575531768  python ok
				||
				\/
	73537877049575531768python ok
"""
import math

def message_encoder(power1, power2, message="python ok"):
	""" log2 based ENCODE """

	# mobile_number1 = 2**power1
	print "pow(2,", power1,") = ", math.pow(2, power1)

	# mobile_number2 = 2**power2
	print "pow(2,", power2,") = ", math.pow(2, power2)


def message_decoder(mobile_number1, mobile_number2, message="python ok"):
	""" log2 based DECODE """

	log2_mobile_number1 = math.log(mobile_number1, 2)
	print "log(",mobile_number1,"2)", " = ", log2_mobile_number1

	log2_mobile_number2 = math.log(mobile_number2, 2)
	print "log(",mobile_number2,"2)", " = ", log2_mobile_number2

	message_encoder(log2_mobile_number1, log2_mobile_number2, message)

def main():	
	if __name__== "__main__":
		mobile_number1 = 7353787704		#first mobile number
		mobile_number2 = 9575531768		#second mobile number
		message = "python ok"			#10 characters including space

		message_decoder(mobile_number1, mobile_number2)

# Calling starter function
main()



