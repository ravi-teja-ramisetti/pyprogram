#program for demonistrating the positional,default and keyword arguments
#posdefkwdargument
def empinfo(eno,ename,sal,dsg,cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(eno,ename,sal,dsg,cnt))
print("="*50)
print("\tEno\tEname\tSal\tDsg\tcnt")
print("="*50)
empinfo(1,"RAVI",7.8,"SE")
empinfo(2,"HARI",7.7,"ME")
empinfo(3,"VENU",4.2,"SA")
empinfo(4,"KLYN",6.8,cnt="JAPAN",dsg="DM")
empinfo(sal=9.8,dsg="CD",eno=5,cnt="USA",ename="PRSD")
empinfo(6,"TSAI",7.8,"SE")