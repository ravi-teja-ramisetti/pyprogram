#program for number generation from 1 to n with positive integers
#numgenex.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid Number".format(n))
else:
    i=1
    while(i<=n):
        print("{}".format(i))
        i=i+1