import time
from threading import Thread

def task(name):
    print(f'task {name} started')
    time.sleep(1)
    print(f'task {name} finished')

t1= Thread(target=task,args=(1, ))
t2= Thread(target=task, args=(2, ))
t3= Thread(target=task, args=(3, ))

t1.start()
t1.join()
t2.start()
print(f't1 ident is {t1.ident}')
print(f't2 ident is {t2.ident}')
print(f't3 ident is {t3.ident}')
t3.start()
