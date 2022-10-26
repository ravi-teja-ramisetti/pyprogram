#program for accepting the integer values
#numgen.py
n=int(input("Enter the n value:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    i=n
    while(i>0):
        print("{}".format(i))
        i=i-1
