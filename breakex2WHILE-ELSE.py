#program for generating the break statement by using the while else
#break
s="PYTHON"
i=0
while(i<len(s)):
    if(s[i]=="H"):
        break
    else:
        print("\t{}".format(s[i]))
    i = i + 1