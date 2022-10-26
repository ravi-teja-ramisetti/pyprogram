#program for calculating the factorial of a positive integer number
#factorialendloopex1.py
n=int(input("Enter the value of:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    #factorial part
    f=1
    for i in range(1,n+1):
        f=f*i
    else:
        print("factorial of {} = {}".format(n,f))