def readvalues():
    lst=[]
    n=int(input("Enter how many elements in list:"))
    if(n<=0):
        return lst
    else:
        for i in range(1,n+1):
            val=int(input("enter {} value in list:".format(i)))
            lst.append(val)
        return lst
def dispsearch():
    lst=readvalues()
    skey=int(input("Enter the element u want to search:"))
    if skey in lst:
        print("SEARCH IS SUCCESSFUL")
    else:
        print("SEARCH IS UNSUCCESSFUL")
dispsearch()
