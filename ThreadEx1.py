#ThreadEx1.py
import threading
def  hello():
	print("-"*50)
	print("Line-5--I am from Hello()")
	print("Line-6--hello() Definition Executed by=",threading.current_thread().name)
	print("-"*50)

def  hi():
	print("*"*50)
	print("Line-11--I am from hi()")
	print("Line-12hi() Definition Executed by=",threading.current_thread().name)
	print("*"*50)

#main program
print("Line-16  I am from Main program:")
print("\nLine-17: Default Naame of thread=-",threading.current_thread().name)
hello()
print("\nLine-19: Default Naame of thread=-",threading.current_thread().name)
hi()
print("\nLine-21: Default Naame of thread=-",threading.current_thread().name)