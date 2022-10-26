#program on arithmetic op on menu driven
#artop
import sys
print("="*50)
print("ARITHMETIC OPERATION")
print("="*50)
print("\t1.addition")
print("\t2.subscration")
print("\t3.multiplication")
print("\t4.division")
print("\t5.mudulo divison")
print("\t6.exponentiation")
print("\t7.exit")
ch=int(input("ENTER THE CHOICE:"))
match(ch):
    case 1:
        a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
        print("({},{})={}".format(a,b,(a+b)))
    case 2:
        a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
        print("({},{})={}".format(a,b,(a-b)))
    case 3:
        a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
        print("({},{})={}".format(a,b,(a*b)))
    case 4:
        a,b=float(input("Enter the value of a:")),float(input('Enter the value of b:'))
        print("({},{}={}".format(a,b,(a/b)))
    case 5:
        a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
        print("({},{})={}".format(a,b,(a//b)))
    case 6:
        a,b=float(input("Enter the value of a;")),float(input("Enter the value of b:"))
        print("({},{})={}".format(a,b,(a**b)))
    case 7:
        print("thank you for using this program !!!!")
        sys.exit()
print("PROGRAM EXECUTION COMPLETED!!!")