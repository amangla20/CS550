''' inspired by: 
	http://anandology.com/python-practice-book/object_oriented_programming.html
	
	other resources:
	https://docs.python.org/3/reference/datamodel.html
	https://docs.python.org/3/library/operator.html
'''

class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __sub__(self, other):
		# fill in code
		return RationalNumber(n, d)

	def __mul__(self, other):
		#fill in code
		return RationalNumber(n, d)

	def __truediv__(self, other):
		# fill in code
		return RationalNumber(n, d)

	# complete this first!
	def __str__(self):
		return 1 # fill in code (replace 1)

	__repr__ = __str__ # what does this do?

def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	print(a) # 1/2
	print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2

main()
