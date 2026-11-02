import os
import time
import requests
import _thread

file_urls = [f"https://dummyimage.com/{i}.png" for i in range(300, 400)]

if not os.path.exists("downloads"):
    os.makedirs("downloads")

def download_file(file_url,cookies,headers,lock):
    try:
        file_name=os.path.basename(file_url)
        file_path = os.path.join("downloads", file_name)
        print(f"Downloading {file_name}...")

        response=requests.get(file_url,cookies=cookies,headers=headers)
        with open(file_path,"wb") as f:
            f.write(response.content)
        print(f"{file_name} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading {file_url} :{e}.")
    finally:
        lock.release()

locks=[]

for file_url in file_urls:
    lock=_thread.allocate_lock()
    lock.acquire()
    locks.append(lock)

    _thread.start_new_thread(download_file,(file_url, {}, {},lock))

for lock in locks:
    while lock.locked():
        time.sleep(0.05)

print("All files downloaded successfully.")
