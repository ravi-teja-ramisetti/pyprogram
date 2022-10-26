#python program for arithmatic operation on figures
#artfig match case
import sys
print("="*50)
print("ARITHEMATIC OPERATIONS")
print("="*50)
print("\t1.circle")
print("\t2.rectangle")
print("\t3.square")
print("\t4.triangle")
print("\t5.exit")
dg=int(input("Enter the diagram:"))
match(dg):
	case 1:
		r=float(input("Enter the radius:"))
		print("area:({})={}".format(r,(r*r)*(3.14)))
	case 2:
		l,b=float(input("Enter the length:")),float(input("Enter the breadth:"))
		print("(area:{},{})={}".format(l,b,(l*b)))
	case 3:
		s=float(input("Enter the side:"))
		print("area:({})={}".format(s,(s*s)))
	case 4:
		b,h=float(input("Enter breadth:")),float(input("Enter height:"))
		print("area:({},{})={}".format(b,h,(b*h)/2))
	case 5:
		print("THANK YOU FOR USING THE PROGRAM !!!")
		sys.exit()
print("program excecution completed!!")