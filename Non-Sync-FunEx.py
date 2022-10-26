#Program for syncronization module
#Non-syncEx.py
import threading,time
def table(n):
	if(n<=0):
		print("{} IS INVALID INPUT".format(n))
	else:
		print("MUL TABLE FOR :{}".format(n))
		for i in range(1,11):
			print("{} x {} = {}".format(n,i,n*i))
			time.sleep(2)
		else:
			print("="*50)
#main program
t1=threading.Thread(target=table,args=(19,))
t2=threading.Thread(target=table,args=(14,))
t3=threading.Thread(target=table,args=(9,))
t1.start()
t2.start()
t3.start()