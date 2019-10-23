class Item:
	def __init__(self, name, uni):
		self.name = name
		self.uni = uni # unicode character representation

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.uni
