import time

def say_hi(name):
    time.sleep(1)
    print('hi', name)

names=['baba','saba','homa','sara']
for name in names:
    say_hi(name)
