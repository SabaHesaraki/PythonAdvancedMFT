import time
from threading import Thread

def task(name):
    print(f"Task : {name} started")
    time.sleep(5)
    print(f"Task : {name} finished")

def check_thread_status(thread):
    time.sleep(3)
    if thread.is_alive():
        print(f"Task : {thread.name} is still running! please wait ...")

t1= Thread(target=task,args=(1, ))
t2= Thread(target=check_thread_status, args=(t1, ))

t1.start()
t2.start()