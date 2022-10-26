#program for generating the voter can vote by age or not
#voterex3.py
n=int(input("Enter the age of the voter:"))
if(n<18)or(n>100):
    print("{} is not eligible to vote".format(n))
else:
    print("{} is eligible to vo5 te:".format(n))