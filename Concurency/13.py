import time
from threading import Thread

def say_hi(name):
    time.sleep(1)
    print('hi',name)

t1=Thread(target=say_hi,args=('baba',))
t2=Thread(target=say_hi,args=('saba',))
t3=Thread(target=say_hi,args=('sanaz',))
t4=Thread(target=say_hi,args=('mama',))

t1.start()
t2.start()
t3.start()
t4.start()