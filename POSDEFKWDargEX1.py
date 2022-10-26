#program for positional arg and default arg
#posidefault&kaywordarg.py
def studinfo(sno,sname,marks,crs="python"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
print("-"*50)
print("\tsno\tsame marks\tcrs")
print("-"*50)
studinfo(1,"PY",55.58)
studinfo(2,"DJ",75.89)
studinfo(3,"FW",88.93)
studinfo(4,sname="HW",marks=92.89,crs="java")
studinfo(crs="c++",marks=85.78,sname="NN",sno=5)
studinfo(crs="SF",marks=35.85,sname="RM",sno=6)
studinfo(marks=99.99,sno=7,crs="DNET",sname="KW")

