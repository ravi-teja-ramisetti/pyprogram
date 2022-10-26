#program for generating the global and local values
#global&localfunEX1.py
a=10
b=20
c=30
d=40
def operation():

    a=1
    b=2
    c=3
    d=4
    print("value of a in local=",a)
    print("value of b in local=",b)
    print("value of c in local=",c)
    print("value of d in local=",d)
    print("\nvalue of a in global=",globals().get('a'))
    print("value of b in global=",globals().get('b'))
    print("value of c in global=",globals().get('c'))
    print("value of d in global=",globals().get('d'))
operation()