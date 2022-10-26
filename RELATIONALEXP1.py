#Program for  pre defined  relational expression with sentence
import re
gd="rohit scored 3 double centuries in odi cricket and rohit is the captain of indian cricket team"
sd="rohit"
res=re.finditer(sd,gd)
print(" '{}' found {} times".format(sd,len(res)))
