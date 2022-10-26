#program for generating the multiplication table of 8
#mulof8.py
n=int(input("ENTER THE TABLE WE WANT:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	i=1
	print("-"*50)
	i=i+1
	for i in range(1,11):
		print("\t{} x {} = {}".format(n,i,n*i))
	else:
		print("-"*50)