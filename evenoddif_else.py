#program for finding even odd zero in if_else statement
#program
n=int(input("Enter the Number:"))
if(n%2==0):
    print("{} is EVEN".format(n))
else:
    if(n%2!=0):
        print("{} is ODD".format(n))
    else:
        print("{} is ZERO".format(n))
