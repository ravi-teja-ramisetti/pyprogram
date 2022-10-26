#program for generating the area and perimeter of the circle by global and local variables
#area&periofcircle.py
PI=3.14
def areaop():
    r=float(input("Enter the radius of circle:"))
    if(r<=0):
        print("{} is Invalid Input".format(r))
    ac=PI*r*r
    print("Area of circle={}".format(ac))
def periop():
    r=float(input("Enter radius of circle:"))
    if(r<=0):
        print("{} is Invalid Input".format(r))
    pc=2*PI*r
    print("Perimeter of circle={}".format(pc))

areaop()
periop()
areaop()
periop()