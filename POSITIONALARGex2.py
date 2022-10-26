#program for positional arguments
#positionalARGex2.py
def studinfo(sno,sname,marks,crs):
    print("\t{},\t{},\t{},\t{}".format(sno,sname,marks,crs))
#main program
print("-"*50)
print("\tsno\tsname\tmarks\tcrs")
print("-"*50)
studinfo(1,"rr",56.23,"python")
studinfo(2,"ee",85.88,"python")
studinfo(3,"uu",95.78,"java")
studinfo(4,"kl",59.69,"c lang")
print("-"*50)