#finding big,small,equal values from the three values from given numbers
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
big="both values are same" if a==b==c else a if a>=b else b if a<b>=c else c
print("big({},{},{}={})".format(a,b,c,big))


small="both values are same" if a==b==c else a if a<=b else b if a>b<=c else c
print("small({},{},{}={}".format(a,b,c,small))