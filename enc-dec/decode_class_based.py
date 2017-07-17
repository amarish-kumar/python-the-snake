"""
	10 June 2017
	============

	7353787704				9575531768  			python ok
		||						||						||
		||						||						||
		\/						\/						\/
	log2(7353787704)		log2(9575531768)		python ok
		||						||
		||						||
		\/						\/
	32.7758403821			33.1567054619							<= ENCODED
		||						||
		||						||
		\/						\/
pow(2, 32.7758403821)	pow(2, 33.1567054619)
		||						||
		||						||
		\/						\/
	7353787704.0			9575531768.0							<= DECODED
"""	

import sys
import math
import re

class MobileMessage:
	def __init__(self, mobile_number1, mobile_number2, message):
		self.mobile_number1 = mobile_number1
		self.mobile_number2 = mobile_number2
		self.message = message
		self.power1 = 0
		self.power2 = 0

	def message_decoder(self):
		""" log2 based DECODE """

		self.power1 = math.log(self.mobile_number1, 2)
		print "\nlog(",self.mobile_number1,"2)", " = ", self.power1

		self.power2 = math.log(self.mobile_number2, 2)
		print "log(",self.mobile_number2,"2)", " = ", self.power2

		
	def message_encoder(self):
		""" log2 based ENCODE """

		# mobile_number1 = 2**power1
		print "pow(2,", self.power1,") = ", math.pow(2, self.power1)

		# mobile_number2 = 2**power2
		print "pow(2,", self.power2,") = ", math.pow(2, self.power2)


	def details(self):
		""" A method that prints details """
		print "\n",
		print "%s%s%s\n"%("="*15, "ENCODE/DECODE LIFE CYCLE", "="*15)

		print "%s%s%s%s"%(" "*6, self.mobile_number1, " "*13, self.mobile_number2)
		print "%s%s%s%s"%(" "*10, "||", " "*20, "||")
		print "%s%s%s%s"%(" "*10, "||", " "*20, "||")
		print "%s%s%s%s"%(" "*10, "\/", " "*20, "\/")

		s1 = str(self.mobile_number1)+",2)"
		s2 = str(self.mobile_number2)+",2)"
		print "%s%s%s%s"%(" "*6, "log("+s1 , " "*5, "log("+s2)

		print "%s%s%s%s"%(" "*10, "||", " "*20, "||")
		print "%s%s%s%s"%(" "*10, "||", " "*20, "||")
		print "%s%s%s%s"%(" "*10, "\/", " "*20, "\/")
		print "%s%s%s%s"%(" "*6, self.power1, " "*10, self.power2)


# Stater function
def main():
	mobile_number1 = 7353787704		#first mobile number
	mobile_number2 = 9575531768		#second mobile number
	message = "python ok"			#10 characters including space

	cmd_args = sys.argv

	print "\n"

	if len(cmd_args) == 4:
		if type(int(cmd_args[1])) == type(67) and type(int(cmd_args[2])) == type(67) and type(cmd_args[3]==type("mobile")):
			if(re.match("[0-9]{10}", cmd_args[1])):
				if(re.match("[0-9]{10}", cmd_args[2])):
					mobile_number1 = int(cmd_args[1]);
					mobile_number2 = int(cmd_args[2]);
				else:
					print "[WARNING]: ", "Mobile number2 should have 10 digits"
			else:
				print "[WARNING]: ", "Mobile number2 should have 10 digits"
		else:
			print "[WARNING]: ", "Mobile number should only contain digits"
	else:
		print "[WARNING]: You need to supply exactly 3 command line parameters"
		print "%s%s"%(" "*11, "MobileNumber1 MobileNumber2 Message")

	mobile1 = MobileMessage(mobile_number1, mobile_number2, message)
	mobile1.message_decoder()
	mobile1.message_encoder()

	mobile1.details()


# Calling starter function
if __name__== "__main__":
	main()