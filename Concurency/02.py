import time
import threading

def say_hi(name):
    time.sleep(1)
    print('hi',name)

threading.Thread(target=say_hi,args=('baba', )).start()
threading.Thread(target=say_hi,args=('sara', )).start()
threading.Thread(target=say_hi,args=('saba', )).start()
threading.Thread(target=say_hi,args=('homa', )).start()