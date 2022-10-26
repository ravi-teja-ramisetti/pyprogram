#program for generating the break statement to generate the prime oe not prime
#prime.py
n=int(input("Enter the value of n : "))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    result=True
    for i in range(2,n):
        if(n%i==0):
            result=False
            break
    if (result == True):
        print("{} is Prime Number".format(n))

    else:
        print("{} is Composite Number".format(n))