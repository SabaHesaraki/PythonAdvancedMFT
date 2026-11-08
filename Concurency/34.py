from time import sleep
from threading import Thread, Semaphore, current_thread

MAX_CONCURRENT = 3
semaphore = Semaphore(MAX_CONCURRENT)

def download(url):
    with semaphore:
        print('Start:',url,'-',current_thread().name)
        sleep(2)
        print('Done:',url)

urls=[f'file-{i}.zip' for i in range(20)]

threads=[Thread(target=download,args=(url,)) for url in urls]

for t in threads:
    t.start()
for t in threads:
    t.join()

print('All downloads finished')