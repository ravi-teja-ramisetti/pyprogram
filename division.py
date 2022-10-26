#division.py--File Name and acts as module Name
from kvr import KvrDivisionError
def    division(a,b):
	if(b==0):
		raise KvrDivisionError
	else:
		return (a/b)

