#Program for getting the multiplication table non thread safety result
#sync-funEx.py
import threading,time
def table(n):
    L.acquire()
    print("Name of the thread of the table:{}".format(threading.current_thread().name))
    if(n<=0):
        print("{} is invalid input".format(n))
    else:
        print("MULTIPLICATION TABLE : {}".format(n))
        for i in range(1,11):
            print("{} x {} = {}".format(n,i,n*i))
            time.sleep(0.1)
        else:
            print("="*50)
    L.release()
#main program
L=threading.Lock()
t1=threading.Thread(target=table,args=(14,))
t2=threading.Thread(target=table,args=(19,))
t3=threading.Thread(target=table,args=(13,))
t4=threading.Thread(target=table,args=(4,))
t1.start()
t2.start()
t3.start()
t4.start()