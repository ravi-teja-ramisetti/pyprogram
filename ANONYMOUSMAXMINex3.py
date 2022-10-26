#program for demonistarting the maximum and minimum values
#ANONYMOUSMAXMINEX3
maxval=lambda r,v:r if r>v else v
minval=lambda r,v:r if r<v else v
#main function
a,b=float(input("Enter the first value:")),float(input("Enter the second value:"))
big=maxval(a,b)
small=minval(a,b)
print("max({},{})={}".format(a,b,big))
print("min({},{})={}".format(a,b,small))