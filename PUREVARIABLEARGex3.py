#PureVarArgsEx3
def   sumop(*n):
	print("-"*50)
	print("Number of Values=",len(n))
	print("-"*50)
	s=0
	for val in n:
		s=s+val
		print("\t{}".format(s))
	else:
		print("sum=",s)
		print("-"*50)

#main program
sumop(10)
sumop(10,20)
sumop(10,20,30)
sumop(10,20,30,40)
sumop(10,20,30,40,50)
sumop()