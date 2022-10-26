#program for odd numbers from positive 1 to 20
#oddloophw.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    i=1
    while(i<=20):
        print("{}".format(i))
        i=i+2