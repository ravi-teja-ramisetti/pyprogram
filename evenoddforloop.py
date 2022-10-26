#program for generating the even odd numbers by using the for loop statement
#evenoddforloop.py
n=int(input("Enter the value of n:"))
if(n<=0):
    print("{} is Invalid Input").format(n)
else:
    print("*"*40)
    print("positive even numbers:{}".format(n))
    print("*"*40)
    for i in range(2,n+1,2):
        print("\t {}".format(i))
    else:
        print("*"*50)
        print("positive even numbers:{}".format(n))
        print("*"*50)
        for i in range (1,n+1,2):
            print("\t {}".format(i))
        else:print("*"*50)