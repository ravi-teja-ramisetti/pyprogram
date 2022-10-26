#program for positive even number starts with 2 to 20
#evenloophw
n=int(input("enter the value of n:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    i=2
    while(i<=20):
        print("{}".format(i))
        i=i+2