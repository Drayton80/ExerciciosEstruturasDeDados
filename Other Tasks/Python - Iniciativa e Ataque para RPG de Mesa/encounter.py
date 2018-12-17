class Encounter:
	# CLASS CONSTRUCTOR:
	def __init__(self, title, creatures):
		self.title = title
		self.creatures = creatures

	# SET METHODS:
	def set_title(self, title):
		self.title = title

	def set_creatures(self, creatures):
		self.creatures = creatures

	# GET METHODS:
	def get_title(self):
		return self.title

	def get_creatures(self):
		return self.creatures