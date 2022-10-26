#program for generating the positive integers by using the for loop statement
#numbergenforloop.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("\t numbers within in {}".format(n))
    print("-"*50)
    for i in range(1,n+1):
        print("{}".format(i))
    else:
        print("="*50)