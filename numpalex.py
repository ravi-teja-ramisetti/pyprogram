#program for palindrome or not palindrome
#numpalex.py
n=int(input("Enter the number:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    on=str(n)
    rn=on[::-1]
    if(on==rn):
        print("{} is palindrome".format(on))
    else:
        print("{} is not palindrome".format(on))