import os
import time
import _thread

def say_hi(name):
    global names
    global counter
    time.sleep(1)
    print('hi', name)
    counter += 1
    if counter == len(names):
        os._exit(0)

names = ['baba','saba','homa','sara']
counter = 0
for name in names:
    _thread.start_new_thread(say_hi,(name,))

input('Please wait until the program execute completely!n')
