class Payment:

	def __init__(self, card_type, card_num, card_date, card_cvv):
		self.cardType = card_type
		self.cardNum = card_num
		self.cardDate = card_date
		self.cardCVV = card_cvv
	
	def validatePayment(self):
		valid_types = ['Visa', 'Discover', 'American Express']
		cardNum_length = 16
		cardCVV_length = 3
		isValid = True
		if self.cardType not in valid_types:
			isValid = False
		elif self.cardNum != cardNum_length:
			isValid = False
		elif self.cardCVV != cardCVV_length:
			isValid = False
		else:
			isValid = True
		return isValid

	
