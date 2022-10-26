#program for generating list and finding maximum and minimum values from the list
#AnonymousFunEx4
def readvalues():
    lst=[]
    n=int(input("Enter the values in list:"))
    if n<=0:
        return lst
    else:
        for i in range(1,n+1):
            val=float(input("Enter {} value:".format(i)))
            lst.append(val)
        return lst
maxvalue=lambda r:max(r)
minvalue=lambda r:min(r)
#main program
l=readvalues()
if len(l)==0:
    print("LIST IS EMPTY")
else:
    print("max({})={}".format(l,max(l)))
    print("min({})={}".format(l,min(l)))