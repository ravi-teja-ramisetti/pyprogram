#PROGRAM FOR GETTING MAX AND MIN VALUUES IN THE THREE POSITIVE INTEGER VALUES
#Anonymous
maxvalue=lambda a,b,c:"All Values are Equal"  if(a==b) and (b==c) else a if(a>=b) and (a>=c) else b if(b>a) and (b>=c) else c
minvalue=lambda a,b,c:"All Values are Equal"  if(a==b) and (b==c) else a if(a<=b) and (a<=c) else b if(b<a) and (b<=c) else c
#main program
a,b,c=float(input("Enter the first value:")),float(input("enter the second value:")),float(input("Enter third value:"))
big=maxvalue(a,b,c)
small=minvalue(a,b,c)
print("max({},{},{})={}".format(a,b,c,big))
print("min({},{},{})={}".format(a,b,c,small))
