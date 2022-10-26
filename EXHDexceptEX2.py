#program for getting the exception in other except form by their division
#divex5
try:
    print("Iam from try block")
    s1=int(input("Enter the first value:"))
    s2=int(input("Enter the second value:"))
    s3=s1/s2
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
else:
    print("-"*50)
    print("first value=",s1)
    print("second value=",s2)
    print("div=",s3)
    print("-"*50)
finally:
    print("iam finally block")