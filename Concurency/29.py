import threading

rlock=threading.RLock()

def rfunc(n):
    if n <=0:
        return
    rlock.acquire()
    try:
        print(f"Thread {threading.current_thread().name} acquired lock with n={n}")
        rfunc(n-1)
        print(f"Thread {threading.current_thread().name} released lock with n={n}")
    finally:
        rlock.release()

threads=[]

for i in range(3):
    t=threading.Thread(target=rfunc, args=(3,),name=f"thread-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have finished execution.")


