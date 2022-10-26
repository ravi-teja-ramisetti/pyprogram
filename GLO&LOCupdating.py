#program for generating or modifing the global variables
#globalANDlocalvar.py
a=10
b=20
c=30
d=40
def operation():
	global c,d
	c=c+1
	d=d+1
	#store c and d values in temp
	tc=c
	td=d
	a=1
	b=2
	c=3
	d=4
	print("val of a local var=",a)
	print("val of b local var=",b)
	print("val of c local var=",c)
	print("val of d local var=",d)
	print("\nval of a global var=",globals().get("a"))
	print("val of b global var=",globals().get("b"))
	print("val of c global var=",tc)
	print("val of d global var=",td)
	res=print(a+b+c+d+globals().get('a')+globals().get('b')+tc+td)

operation()