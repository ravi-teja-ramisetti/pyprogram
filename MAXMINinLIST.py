# Program for finding max and min of list of elements by accepting elements dynamically from KBD
# MaxMinEx2.py
def readvalues():
    lst = []
    n = int(input("Enter How Many Value sum u want to find:"))
    if (n <= 0):
        return lst
    else:
        for i in range(1, n + 1):
            val = float(input("Enter {} Value:".format(i)))
            lst.append(val)
        return lst
def findmaxminvalues():
    l=readvalues()
    if (len(l) == 0):
        print("List is empty")
    else:
        print("Max({})={}".format(l, max(l)))
        print("Min({})={}".format(l, min(l)))
# main program
findmaxminvalues()




