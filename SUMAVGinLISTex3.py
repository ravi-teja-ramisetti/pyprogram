#program for sum and avg of elements in list
#sumavgex3.py
def readvalues():
    lst=[]
    n=int(input("Enter the elements to join in list:"))
    if(n<=0):
        return lst
    else:
        for val in range(1,n+1):
            val=int(input("Enter {} in list:".format(val)))
            lst.append(val)
        return lst
def sumavg(lstobj):
    if len(lst)!=0:
        s=sum(lstobj)
        print("elements in list:{}".format(lstobj))
        print("sum={}".format(s))
        print("avg={}".format(s/len(lstobj)))
    else:
        print("list is empty")
#main program
lst=readvalues()
sumavg(lst)
