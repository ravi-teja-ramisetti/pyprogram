#Program for addition of two numbers with Normal and Anonymous Functions
#ANONYMOUSFUNex2.py
def addop(a,b):
	c=a+b
	return c
addop=lambda a,b:a+b
#main program
res=addop(float(input("enter the first value:")),float(input("enter the second value:")))
print("add=",res)
print("type of addop",type(addop))