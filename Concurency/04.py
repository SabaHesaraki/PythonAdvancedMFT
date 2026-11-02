import time
import _thread

def say_hi(name):
    time.sleep(1)
    print('hi', name)

names=['baba','saba','homa','sara']
for name in names:
    _thread.start_new_thread(say_hi,(name, ))

input("wait for the result and press enter!\n")
