#Program for modifing the value of global variable by using global keyword
#globalkwdex1.py
a=10
b=20
def statement1():
    global a,b
    a=a+1
    b=b+2
def statement2():
    global a,b
    a=a*2
    b=b*2
print("val of a before statement1()=",a)
print("val of b before statement2()=",b)
statement1()
print("\nVal of a after statement1()=",a)
print("val of b after statement2()=",b)
statement2()
print("\nVal of a after statement1()=",a)
print("val of b after statement2()=",b)