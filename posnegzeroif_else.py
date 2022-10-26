#program for acceptance of pos neg and zero in integers by if_else statement
#program
n=int(input("Enter the Number:"))
print("="*50)
if(n>0):
    print("{} is +VE".format(n))
else:
    if(n<0):
        print("{} is -VE".format(n))
    else:
        if(n==0):
            print("{} is ZERO".format(n))
print("="*50)
print("program excecuted!!!!")
print("="*50)

