from threading import Thread

number = 0

def add():
    global number
    for i in range(100000):
        number +=1

def subtract():
    global number
    for i in range(100000):
        number -=1

thread1=Thread(target=add)
thread2=Thread(target=subtract)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(number)