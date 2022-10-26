#Main Program
#DivisionDemo.py
from division import division
from Kvr import KvrDivisionError
try:
	x=int(input("Enter First Value:"))
	y=int(input("Enter Second Value:"))
	res=division(x,y) # Function Call
except KvrDivisionError:
	print("\nDon't Enter Zero for Den...")
except ValueError:
	print("\nDon't Enter strs,symbols and alpha-numerics")
else:
	print("Div=",res)
finally:
	print("\ni am from finally block")


#Note: Deveplopment of Main program where can handle the exception---Phase-III