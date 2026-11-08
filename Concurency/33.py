from time import sleep
from threading import Thread, Semaphore, current_thread

lock = Semaphore(2)

def worker():
    acquired = lock.acquire(timeout=1)
    if not acquired:
        print('Skipped:', current_thread().name)  
        return
    try:
        print('Working:', current_thread().name)
        sleep(2)
    finally:
        lock.release()

threads = [Thread(target=worker) for _ in range(5)]

for t in threads:
    t.start()