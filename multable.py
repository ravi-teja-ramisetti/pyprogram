#program for multiplication table
#multable.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid")
else:
    i=1
    while(i<=10):
        print("{} x {} = {}".format(n,i,n*i))
        i=i+1