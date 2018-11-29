class Cart:
	def __init__(self):
		self.numItems = 0
		self.items = []

	def add(self, item):
		self.numItems += 1
		self.items.append(item)


