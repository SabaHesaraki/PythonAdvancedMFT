import threading
import time
import _thread as thread

counter=0

lock=thread.allocate_lock()

def add(thread_id):
    global counter
    for _ in range(100):
        with lock:
            temp=counter
            temp+=1
            time.sleep(0.01)
            counter=temp
            print(f"Thread {thread_id}: {counter}")

def subtract(thread_id):
    global counter
    for _ in range(100):
        with lock:
            temp=counter
            temp-=1
            time.sleep(0.01)
            counter=temp
            print(f"Thread {thread_id}: {counter}")

thread.start_new_thread(add,(1,))
thread.start_new_thread(subtract,(2,))

time.sleep(5)

print(f"Final counter value: {counter}")
