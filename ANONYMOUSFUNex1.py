#program for demonistrating the anonymous fuction
#ANONYMOUSFUNex.py
def sumop(a,b):
    c=a+b
    return c
sumop=lambda a,b:a+b
#function call
res=sumop(10,20)
print("sum=",res)
print("type of function=",type(sumop))
print("-"*50)
res1=sumop(100,500)
print("add=",res1)
print("type of sumop=",type(sumop))