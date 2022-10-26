#program for generating the marks card in subjects of c,c++,python with each 100 marks
#markscardex4.py
#accept the student number
while(True):
    sno= int(input("Enter the student number:"))
    if(sno>0):
        break
    print("{} is Invalid Input".format(sno))
#accept the student name
sname=input("Enter the name of student:")
#accept the student c lang marks
while(True):
    cm=int(input("Enter the c lang marks:"))
    if(cm>0)and(cm<100):
        break
    print("{} IS Invalid marks".format(cm))
#accept the c++ marks
while(True):
    cppm=int(input("Enter the c++ lang marks:"))
    if(cppm>0)and(cppm<100):
        break
    print("{} is Invalid marks".format(cppm))
#accept the python lang marks
while(True):
    pym=int(input("Enter the python marks:"))
    if(pym>0)and(pym<100):
        break
    print("{} is invalid Marks".format(pym))
#accept the total marks by student
totmarks=(cm+cppm+pym)
#accepting percentage of the student
percent=(totmarks/300)*100
if(cm<40) or (cppm<40) or (pym<40):
    grade="Fail"
else:
    if(totmarks>=250)and(totmarks<=300):
        grade="DISTINTION CLASS"
    elif(totmarks>=200)and(totmarks<=249):
        grade="First Class"
    elif(totmarks>=150)and(totmarks<=199):
        grade="SECOND CLASS"
    elif(totmarks>=120)and(totmarks<=149):
        grade="Third Class"
print("+"*50)
print("student report card")
print("-"*50)
print("student number:{}".format(sno))
print("student name:{}".format(sname))
print("student marks in c lang:{}".format(cm))
print("student marks in cpp lang:{}".format(cppm))
print("stident marks in python:{}".format(pym))
print("*"*50)
print("total marks got by student: {}".format(totmarks))
print("percentage of student:{}".format(percent))
print("grade of the student:{}".format(grade))
print("*"*50)