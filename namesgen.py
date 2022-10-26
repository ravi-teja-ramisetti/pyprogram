n=int(input("Enter the number of names:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    l=list()
    for i in range(1,n+1):
        names=input("Enter {} value".format(i))
        l.append(names)
    else:
        print("="*50)
        print("Names=",l)
        print("="*50)
        omn=input("enter the removing name:")
        for names in l:
            if(names==omn):
                break
            else:
                print("{}".format(names))