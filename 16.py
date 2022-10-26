#PolyEx2.py
class Circle:
	def  area(self,r):  # Original Method
		self.ac=3.14*r**2
		print("Area of Circle=",self.ac)
		#super().area(float(input("Enter Value:")))----AttributeError: 'super' object has no attribute 'area'

class Square(Circle):
	def area(self,s):  # overridden Method
		self.sa=s**2
		print("Area of Square=",self.sa)
		print("-"*40)
		super().area(float(input("Enter Radious:")))

class Rect(Square):
	def area(self,l,b):
		self.ar=l*b
		print("Area of Rect=",self.ar)
		print('-'*50)
		super().area(float(input("Enter Side:")))

#main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")))

