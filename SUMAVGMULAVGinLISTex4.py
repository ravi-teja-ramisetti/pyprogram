#program on sum and avg in list
import math
def readvalues():
    lst=[]
    n=int(input("Enter the number of elements to list:"))
    if (n<=0):
        return lst
    else:
        for k in range(1,n+1):
            val=int(input("Enter {}  in value :".format(k)))
            lst.append(val)
        return lst
#main program
def sumavg(lstobj):
    if len(lst)!=0:
        m=math.prod(lstobj)
        s=math.fsum(lstobj)
        print("Elements in list:{}".format(lstobj))
        print("sum={}".format(s))
        print("mul={}".format(m))
        print("sum avg={}".format(s/len(lstobj)))
        print("mulavg={}".format(m/len(lstobj)))
    else:
        print("list is empty")
lst=readvalues()
sumavg(lst)