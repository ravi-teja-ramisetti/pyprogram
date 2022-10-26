#program for getting the sum of values and average of values
#sumavgex1
def sumavg(lstobj):
    s=0
    for val in lstobj:
        s=s+val
    else:
        print("elements:{}".format(lstobj))
        print("sum={}".format(s))
        print("avg={}".format(s/len(lstobj)))
#main program
lst=[10,20,50,70]
sumavg(lst)