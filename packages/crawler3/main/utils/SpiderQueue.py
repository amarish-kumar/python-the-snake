class SpiderQueue:
	def __init__(self, spiderName, spiderAge):
		self.name = spiderName
		self.age = spiderAge

	def get_details(self):
		return "Name - " + self.name + ", Age - " + str(self.age) + " years"