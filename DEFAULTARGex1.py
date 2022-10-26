#program for default argument
#defaultargex1.py
def studinfo(sno,sname,marks,crs="PYTHON"):
	print("\t{},\t{},\t{},\t{}".format(sno,sname,marks,crs))
print("-"*50)
print("\tsno\tsname\tmarks\tcrs")
print("-"*50)
studinfo(1,"rjo",52)
studinfo(2,"rsd",45)
studinfo(3,"rol",85)
studinfo(4,"red",78)
print("-"*50)
