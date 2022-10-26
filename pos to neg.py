#changing the sign from positive to negitive value of numbers
#pos to neg number
n=int(input("enter the numbewr:"))
result="+ve" if n>0 else "-ve" if n<0 else "zero"
print("{} is {}".format(n,result))