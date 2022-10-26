#program for getting two integer values to get their division
try:
    print("program exceution started")
    a=input("Enter the first value:")
    b=input("Enter second number:")
    a=int(a)
    b=int(b)
    c=a/b
    print("div=",c)
except ZeroDivisionError:
    print("divisible by zero is not valid")
except ValueError:
    print("values does not in form of symbols,alphanumerics and strs")
else:
    print("-"*50)
    print("first number=",a)
    print("second number=",b)
    print("div=",c)
    print("-"*50)
