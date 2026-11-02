import time
import _thread

def say_hi(name):
    global names
    global counter
    time.sleep(1)
    print('hi', name)
    counter += 1

names=['baba','saba','homa','sara']
counter = 0
for name in names:
    _thread.start_new_thread(say_hi, (name, ))

while True:
    if counter == len(names):
        break
    time.sleep(0.1)