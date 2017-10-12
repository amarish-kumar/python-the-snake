class TimeTools:
	def __init__(self, toolName, toolAge):
		self.name = toolName
		self.age = toolAge

	def get_details(self):
		return "Name - " + self.name + ", Age - " + str(self.age) + " years"