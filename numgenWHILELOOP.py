#program for calculating the positive integers from n to 1 by loop statemenet
#nto1.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    i=n
    while(i>0):
        print("{}".format(i))
        i=i-1