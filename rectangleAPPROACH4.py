def   areaop():
	l=float(input("Enter length of rectabgle:"))
	b=float(input("Enter breadth of rectangle:"))
	a=l*b
	return l,b,a
#main program
k,v,r=areaop()  # Function Call with Multi Line assignment
print("area({},{})={}".format(k,v,r))
print("===========OR=================")
hyd=areaop() # Function Call---here hyd   is an object of type <class, tuple>
print("area({},{})={}".format(hyd[0],hyd[1],hyd[2]))