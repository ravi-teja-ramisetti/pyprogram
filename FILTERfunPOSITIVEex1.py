#program for getting positive elements from the list creating new list in filter function
def posnum(n):
    if(n>0):
        return True
    else:
        return False
lst=[10,250,78,45,-99,-45,99.99,78,-52,78,-96,89]
n=filter(posnum,lst)
posnum=list(n)
print("Original list of number=",lst)
print("Positive list of numbers=",posnum)