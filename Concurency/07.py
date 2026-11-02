import time
import _thread

def say_hi(name,lock):
    time.sleep(1)
    print('hi', name)
    lock.release()

if __name__ == '__main__':
    names=['baba','saba','homa','sara']
    locks=[]

    for name in names:
        lock=_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
        _thread.start_new_thread(say_hi,(name,lock))

    for lock in locks:
        lock.acquire()

    print('Successfully Done!')
