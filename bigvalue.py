a=float(input("enter first value:"))
b=float(input("enter second value:"))
c=float(input("enter third value:"))


big="both values are same" if a==b==c else a if a>b else b if b>c else  c
print("{},{},{}={}".format(a,b,c,big))

small="both values are same" if a==b==c else a if a<=b else b if b<=c else c
print("{},{},{}={}".format(a,b,c,small))

big="both values are same" if a==b==c else a if b<=a>c else b if a<b>=c else c
small="both values are same" if a==b==c else a if b>=a<c else b if a>b<=c else c
print("{},{},{}={}".format(a,b,c,big))
print("{},{},{}={}".format(a,b,c,small))