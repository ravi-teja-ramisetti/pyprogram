#Program for factors generation by for loop statememt
#factorsfoorloop
n=int(input("Enter value of n:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Factors of {}".format(n))
    print("="*50)
    for i in range(1,n):
        if(n%i==0):
            print("{}".format(i))