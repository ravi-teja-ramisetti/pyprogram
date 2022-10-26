#program for acceptance of integer as positive negitive and zero in simple if method
#progon+-0
n=int(input("Enter the number:"))
if(n==0):
    print("{} is ZERO".format(n))
if(n>0):
    print("{} is -VE".format(n))
if(n<0):
    print("{} is +VE".format(n))
print("\n PROGRAM EXECUTION SUCCESSFULLY!!!!")