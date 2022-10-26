a=10
def statement1():
    global a
    a=a+1
def statement2():
    global a
    a=a*10
print("value of a before updating=",a)
print("value of a before updating=",a)
statement1()
print("\nvalue of a after updation=",a)
statement2()
print("\nvalue of a after updation=",a)