import re
gd="python is an oop language and case sensitive"
sd="python"
res=re.search(sd,gd)
if(res!=None):
	print("Search is Successfull")
	print("{} is found in beg index: {} and end index:{}".format(sd,res.start(),res.end()))
else:
	print("Search is UnSuccessful")