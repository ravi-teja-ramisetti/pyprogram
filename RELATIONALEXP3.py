#RegExpr4.py
import re
gd="raviteja came to hyd long back ago after 3 months raviteja got a best package job in best company and finally raviteja dream comes true and then raviteja lovedone divya makes him happy and lived together happily"
sd="and"
res=re.finditer(sd,gd)
ctr=0
for k in res:
	print("START INDEX:{}  END INDEX:{} AND VALUE:{}".format(k.start(),k.end(),k.group()))
	ctr=ctr+1
else:
	print("{} is found {} times".format(sd,ctr))
