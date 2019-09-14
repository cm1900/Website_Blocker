import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
test_host = 'hosts'
redirect = '127.0.0.1'
blocked_sites = ['www.facebook.com', 'facebook.com', 'www.twitter.com',
'twitter.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
    else:
        print("Offline...")
    time.sleep(10)