import time
from threading import Thread

def task(name):
    print(f"Task : {name} started")
    time.sleep(1)
    print(f"Task : {name} finished")

t1= Thread(target=task,args=(1, ))
t2=Thread(target=task, args=(2, ))

t1.start()
t2.start()
t1.join()
t2.join()
print("End of programming")