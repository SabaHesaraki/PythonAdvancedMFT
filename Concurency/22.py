import time
from threading import Thread, current_thread

def task():
    print(f"task {current_thread().name} started")
    time.sleep(1)
    print(f"task {current_thread().name} finished")

Thread(target=task).start()

