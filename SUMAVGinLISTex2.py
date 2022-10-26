#program for sum and average in list of elements
#sumavgex2.py
def sumavg(lstobj):
    s=sum(lstobj)
    print("elements in list:{}".format(lstobj))
    print("sum={}".format(s))
    print("avg={}".format(s/len(lstobj)))
#main program
lst=[10,9,8,4,6,7]
sumavg(lst)