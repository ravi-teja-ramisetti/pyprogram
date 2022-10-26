#program for calculating the multiples of 3 by using the forloop statement
#mul3forloop.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Multiples of the (3) : {}".format(n))
    print("="*50)
    for i in range(3,n+3,3):
        print("\t {}".format(i))
    else:
        print("="*50)