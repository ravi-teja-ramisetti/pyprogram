#program for generating the factorial of the positive integers by using math modules
#factorialmathex2.py
import math
n=int(input("Enter the value :"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    f=math.sqrt(n)
    print("factorial of {} = {}".format(n,f))