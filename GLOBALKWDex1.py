#using the global keyword to modify the keyword value
a=10
def statement():
    global a
    a=a+1
print("value of a value before modification=",a)
statement()
print("\nValue of a value after modification=",a)

