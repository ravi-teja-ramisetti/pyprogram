#Program for finding biggest and smallest among three numerical values
#bigex3.py
a=float(input("Enter First Value:"))  # a=10
b=float(input("Enter Second Value:")) # b=5
c=float(input("Enter Third Value:")) # c=2
big="All Values are Equal"  if(a==b==c) else a if(a>=b>=c) else b if(b>a>=c) else c
print("big({},{},{})={}".format(a,b,c,big))
small="All Values are Equal"  if(a==b==c) else a if(a<=b<=c) else b if(b<a<=c) else c
print("small({},{},{})={}".format(a,b,c,small))