def d():
	print "ok"


class Person(object):
	"""constructor for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

	def method(self):
		print "Method: ", self.name

	@classmethod
	def class_method(cls):
		print cls.self


		