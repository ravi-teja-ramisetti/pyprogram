#program for generating nat num , sq numbers , cube numbers by using for loop statement
#natsqcubeforloop.py
n=int(input("Enter the value of n:"))
if(n<=0):
	print("{} is Invalid Input".format(n))
else:
	s,ss,cs=0,0,0
	print("*"*50)
	print("nat num \t\t sq num \t\t\tcube num")
	print("*"*50)
	for i in range(1,n+1):
		print("\t {}\t\t\t{}\t\t\t {}".format(i,i**2,i**3))
		s=s+i
		ss=ss+i**2
		cs=cs+i**3
	else:
		print("="*50)
		print("     {}      {}       {}".format(s,ss,cs))
