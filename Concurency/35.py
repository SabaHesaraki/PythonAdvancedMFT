from time import sleep
from threading import Thread, BoundedSemaphore, current_thread

lock = BoundedSemaphore(2)

def add():
    try:
        lock.acquire()
        print('Downloading image by', current_thread().name)
        sleep(2)
        lock.release()
        lock.release()                  
    except ValueError:
        print('Can not release', current_thread().name)

threads = [Thread(target=add) for _ in range(13)]

for t in threads:
    t.start()