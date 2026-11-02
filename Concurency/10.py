import os
import time
import requests
import _thread

file_urls = [f"https://dummyimage.com/{i}.png" for i in range(300, 400)]

REPORT_FILE= "downloads/download_report.txt"

os.makedirs("downloads", exist_ok=True)


with open(REPORT_FILE,"w") as f:
    f.write("Download Report:\n")
    f.write("================\n")

report_lock=_thread.allocate_lock()

def download_file(file_url, cookies,headers,download_lock):
    file_name= os.path.basename(file_url)
    file_path=os.path.join("downloads",file_name)

    status_message=""

    try:
        print(f"Downloading {file_name}...")
        response=requests.get(file_url,cookies=cookies,headers=headers)
        with open(file_path,"wb") as f:
            f.write(response.content)

        status_message=f"SUCCESS :{file_name} downloaded successfully.\n"
        print(status_message)

    except Exception as e:
        status_message=f"FAILED :{file_name} - Error :{e}.\n"
        print(status_message)

    finally:
        download_lock.release()

        report_lock.acquire()
        try:
            with open(REPORT_FILE,"a") as f:
                f.write(f"{status_message}\n")
        finally:
            report_lock.release()

download_locks=[]

for file_url in file_urls:
    lock=_thread.allocate_lock()
    lock.acquire()
    download_locks.append(lock)

    _thread.start_new_thread(download_file,(file_url, {}, {},lock))

for lock in download_locks:
    while lock.locked():
        time.sleep(0.05)

print("All download attempts finished. Check download_report.txt for details.")

