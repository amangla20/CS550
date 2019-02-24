# initializing the barriers/walls class
# this class uses getters and setters to get the x position and y position of the top left corner of the walls since they are "rects", and the width and height dimensions of the walls. It also uses getters and setters to get the kind of the barrier, where there are three different types of barriers that appear in different colors on the screen.
class Create:
	# constructor of the Create class to construct the barriers
	def __init__(self, posx, posy, dimw, dimh, kind):
		self.posx = int(posx)
		self.posy = int(posy)
		self.dimw = int(dimw)
		self.dimh = int(dimh)
		self.kind = int(kind)

	# getters and setters
	def getPosx(self):
		return self.posx
	def setPosx(self):
		self.posx = int(posx)
	def getPosy(self):
		return self.posy
	def setPosy(self):
		self.posy = int(posy)
	def getDimw(self):
		return self.dimw
	def setDimw(self):
		self.dimw = int(dimw)
	def getDimh(self):
		return self.dimh
	def setDimh(self):
		self.dimh = int(dimh)
	def getKind(self):
		return self.kind
	def setKind(self):
		self.kind = int(kind)
