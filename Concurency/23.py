import time
from threading import Thread, active_count

def task():
    time.sleep(1)

t1=Thread(target=task)
t2=Thread(target=task)

t1.start()
print(active_count())
t2.start()
print(active_count())