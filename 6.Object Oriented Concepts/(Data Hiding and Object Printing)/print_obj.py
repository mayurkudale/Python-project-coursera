class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return "Test: print using __repr__ a:%s b:%s" % (self.a, self.b)


# Driver Code
t = Test(1234, 5678)
print(t)

#If no __str__ method is defined, print t (or print str(t)) uses __repr__.
