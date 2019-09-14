#To use, test_host must be replaced with host_path
#and command window must be opened as administrator

import time
from datetime import datetime as dt

host_path = r'C:\Windows\System32\drivers\etc\hosts'
test_host = r'C:\Users\Christino\OneDrive\Documents\Website_Blocker\hosts'
redirect = '127.0.0.1'
blocked_sites = ['www.facebook.com', 'facebook.com', 'www.twitter.com',
'twitter.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        #Working hours
        with open(test_host, 'r+') as file:
            content = file.read()
            for website in blocked_sites:
                if website in content:
                    pass
                else:
                    file.write('\n{} {}'.format(redirect, website))
    else:
        #Offline hours
        with open(test_host, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_sites):
                    file.write(line)
            file.truncate()
    time.sleep(10)