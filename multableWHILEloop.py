#generating the multiplication table for the positive integer by using statement
#multablegen.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is  Invalid Input".format(n))
else:
    i=1
    print("-"*50)
    print("mul of the :{}".format(n))
    print("-"*50)
    while(i<=10):
        print("{} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("*"*50)
