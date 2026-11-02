import time
import _thread

def say_hi(name , delay_lock):
    time.sleep(1)
    print('hi', name)
    delay_lock.release()

names = ['baba', 'saba', 'homa', 'sara','fatima']

locks=[]
for name in names:
    lock=_thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
    _thread.start_new_thread(say_hi, (name, lock))

for lock in locks:
    while lock.locked():
        time.sleep(0.1)

print("All done!")
