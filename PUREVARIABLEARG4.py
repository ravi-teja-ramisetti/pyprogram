#PureVarArgsEx3
def disp(*a):
	print("NUMBER OF VALUES IN A=",len(a))
	for val in a:
		print("{}".format(val))
	else:
		print("-"*50)
	s=0
	for val in a:
		s=s+val
		print("{}".format(s))
	else:
		print("sum=",s)


disp(10,20,30)