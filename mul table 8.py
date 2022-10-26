#program for generating the multiplication table by using the if else statement
#mulof8.py
n=int(input("Enter the table we want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("*"*50)
    print("mul table for:{}".format(n))
    print("*"*50)
    i=1
    while(i<=10):
        print("\t{} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("="*50)