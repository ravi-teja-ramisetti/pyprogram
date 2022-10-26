def addop():
    a=float(input("Enter value of a:"))
    b=float(input("Enter the value of b:"))
    c=a+b
    return a,b,c
r,v,t=addop()
print("{},{}={}".format(r,v,t))
print("===============or==================")
tej=addop()
print("{},{}={}".format(tej[0],tej[1],tej[2]))

