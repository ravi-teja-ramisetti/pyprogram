#python program on getting odd positive integers by using the while loop statement
#oddloop.py
n=int(input("Enter the value of n:"))
if(n<=0):
	print("{} is Invalid".format(n))
else:
	i=1
	while(i<=20):
		print("{}".format(i))
		i=i+2