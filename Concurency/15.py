import time
from threading import Thread

class MyThread(Thread):
    def __init__(self , target,args):
            super().__init__()
            self.target=target
            self.args=args

    def run(self):
        self.target(*self.args)

def say_hi(name):
    time.sleep(1)
    print(f"Hi {name}")

t1= MyThread(target=say_hi,args=("Saba", ))
t2= MyThread(target=say_hi,args=("Sanaz", ))
t3= MyThread(target=say_hi,args=("Mohi", ))
t4= MyThread(target=say_hi,args=("Fatima", ))

t1.start()
t2.start()
t3.start()
t4.start()