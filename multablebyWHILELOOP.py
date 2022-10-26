#program for generating the mul table of 8
#mulof8.py
n=int(input("Enter the table num we want:"))
if(n<=0):
	print("{} is Invalid Input".format(n))
else:
	i=1
	while(i<=20):
		print("\t{} x {} = {}".format(n,i,n*i))
		i=i+1