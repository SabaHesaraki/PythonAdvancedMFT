import time
from threading import Thread

def send_welcome_email(user):
    print(f"sending email to {user} ...")
    time.sleep(1)
    print(f"email sent to {user}")

users=["ali@example.com" , "saba@example.com" , "sanaz@example.com"]

threads=[Thread(target=send_welcome_email,args=(user, )) for user in users]

for t in threads:
    t.start()
for t in threads:
    t.join()

print('all emails have been sent')
