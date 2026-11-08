import time
from threading import Thread

def task():
    time.sleep(1)

t1 = Thread(target=task)

t1.start()

print(t1.name)
print("old name is:",t1.name)
t1.name="Great thread 1"
print("new name is:",t1.name)