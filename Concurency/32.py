from time import sleep
from threading import Thread, Semaphore, current_thread

lock = Semaphore(2)

def download():
  with lock:
    print('Downloading image by', current_thread().name)
    sleep(1)
   

threads=[Thread(target=download) for _ in range(5)]

for t in threads:
    t.start()