#program for default argument
#defaultarg.py
def studinfo(sno,sname,marks,crs="python",cnt="india"):
    print("\t{},\t{},\t{},\t{},\t{}".format(sno,sname,marks,crs,cnt))
#main program
print("-"*50)
print("\tsno\tsane\tmarks\tcrs\tcnt")
print("-"*50)
studinfo(1,"res",75)
studinfo(2,"ret",80)
studinfo(3,"reu",85)
studinfo(4,"rev",90)
studinfo(5,"rew",95,"java","usa")
studinfo(6,"rex",99)
print("-"*50)