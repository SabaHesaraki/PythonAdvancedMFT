import time
from threading import Thread

def download(url):
    print(f'downloading {url}')
    time.sleep(2)
    print(f'finished {url}')

urls=['a.com','b.com','c.com','d.com']

start = time.time()
threads=[Thread(target=download,args=(url,)) for url in urls]

for t in threads:
    t.start()
for t in threads:
    t.join()

print('all downloads took %.1fs' % (time.time() - start)) 