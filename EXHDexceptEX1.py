#program for  getting the exceptions and getting their dividion
#divex3.py
try:
	print("Iam from the try block")
	s1=input("\nEnter the first value:")
	s2=input("Enter the second value:")
	a=int(s1)
	b=int(s2)
	c=a/b
except (ZeroDivisionError,ValueError):
	print("-"*50)
	print("DONT ENTER THE DIVISION BY ZERO")
	print("DONT ENTER THE STRS,SYMBOLS AND ALPHA NUMERICS")
	print("-"*50)
else:
	print("-"*50)
	print("first value=",a)
	print("second value=",b)
	print("div=",c)
	print("-"*50)
finally:
	print("iam from finally block")