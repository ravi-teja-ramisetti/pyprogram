#RELATIONAL EXPRESSION
import re
res=re.finditer("[A-Z]","qwertyui/852opASdrtyHJKLzxcvBNM@#$%^&*()_+rf98qasSF654CGJN3210364")
for x in res:
	print("START INDEX:{}  END INDEX:{}  AND VALUE:{}".format(x.start(),x.end(),x.group()))
