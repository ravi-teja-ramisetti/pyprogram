#FirstTread.py
import threading
def hlo():
    print("="*50)

t=threading.current_thread()
print(t.name)
print("========or=========")
print("default threading name of thread=",threading.current_thread())
print("number of active threads=",threading.active_count())

