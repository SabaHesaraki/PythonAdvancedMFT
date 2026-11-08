import time
from threading import Thread

def task(name):
    print(f'task {name} started')
    time.sleep(1)
    print(f'task {name} finished')

def check_thread_status(thread):
    time.sleep(3)
    if thread.is_alive():
        print(f"{thread.name} is still running! please wait ...")

t1 = Thread(target=task, args=(1, ))
t2 = Thread(target=check_thread_status, args=(t1, ), daemon=True)

t1.start()
t2.start()