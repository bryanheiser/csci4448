from payment import Payment
from item import Item

class Customer:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.cart = []

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def checkout(self):
		total = 0
		for item in self.cart:
			total += item.get_price()
		return total

	def addToCart(self, item):
		self.cart.append(item)

	def removeFromCart(self, item):
		for i in range(len(self.cart)):
			if item.get_name() == self.cart[i].get_name():
				del self.cart[i]
				return True
		return False

