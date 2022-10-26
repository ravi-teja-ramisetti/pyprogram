#program for generating the break statement by using the text
#break
s="python is an oop language"
for k in s:
    if(k=="o") or (k=="i"):
        continue
    else:
        print("\t {}".format(k))