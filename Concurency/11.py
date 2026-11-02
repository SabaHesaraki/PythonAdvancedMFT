import _thread as thread
import time

counter=0

lock=thread.allocate_lock()

def add(thread_id):
    global counter
    for _ in range(100):
        lock.acquire()
        temp=counter
        temp +=1
        time.sleep(0.01)
        counter=temp
        print(f"Thread {thread_id}: {counter}")
        lock.release()

def subtract(thread_id):
    global counter
    for _ in range(100):
        lock.acquire()
        temp=counter
        temp -=1
        time.sleep(0.01)
        counter=temp
        print(f"Thread {thread_id}: {counter}")
        lock.release()

thread.start_new_thread(add,(1,))
thread.start_new_thread(subtract,(2,))

time.sleep(5)

print(f"Final counter value: {counter}")