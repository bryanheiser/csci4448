class Item:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity

	def get_name(self):
		return self.name
	
	def get_price(self):
		return self.price

	def get_quantity(self):
		return self.quantity

	def changePrice(self, new_price):
		self.price = new_price

	def increaseQuantity(self):
		self.quantity += 1
	
	def decreaseQuantity(self):
		isValid = False
		if self.quantity > 0:
			self.quantity -= 1
			isValid = True
		return isValid

	
