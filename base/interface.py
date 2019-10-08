import requests
import time
import os
# url = 'http://127.0.0.1:5000/login'
# data = {'username': 'zengwenhai', 'password': '123456'}
# r = requests.post(url=url, data=data)
# print(r.text)

foramt_time = '%Y-%m-%d %H:%M:%S'
nowtime = time.strftime(foramt_time, time.localtime())
print(nowtime)

reportname = 'report%s.html' % nowtime
print(reportname)

print(os.path.dirname(os.path.dirname(__file__)))