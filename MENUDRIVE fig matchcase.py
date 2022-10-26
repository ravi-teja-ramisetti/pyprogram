#areas of fig
#areas fir fig
import sys
print("="*50)
print("calculation of areas")
print("="*50)
print("\t1.circle")
print("\t2.rectangle")
print("\t3.square")
print("\t4.triangle")
print("\t5.exit")
dig=int(input("Enter the fig number:"))
match(dig):
    case 1:
        r=float(input("Enter the radius:"))
        print("area:({})={}".format(r,(r*r)*(3.14)))
    case 2:
        l,b=float(input("Enter the length:")),float(input("Enter the bredth:"))
        print("area:({},{})={}".format(l,b,(l*b)))
    case 3:
        s=float(input("Enter the side:"))
        print("area:({})={}".format(s,s*s))
    case 4:
        b,h=float(input("Enter bredth:")),float(input("Enter the height:"))
        print("area:({},{})={}".format(b,h,(b*h)/2))
    case 5:
        print("thanks for using my program=====RAVITEJA")
        sys.exit()
print("PROGRAM EXCECUTED SUCCESFULLY!!!!")