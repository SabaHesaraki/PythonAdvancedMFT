import time
from threading import Thread, enumerate

def task():
    time.sleep(1)

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
print(enumerate())
t2.start()
print(enumerate())
