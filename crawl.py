import json
import requests
import thread


def get():
    url = 'http://backend.igengmei.com/api/live/enter?platform=iPhone&os_version=10.3.3&version=7.5.0&model=iPhone%206s%20Plus&release=1&idfa=0ADCBC49-C27F-4F2A-9767-A3765B47076B&idfv=D5496DD5-4ABF-488C-A4F9-DC032A0AC77D&device_id=0ADCBC49-C27F-4F2A-9767-A3765B47076B&channel=App%20Store&app_name=gengmeiios&current_city_id=wuhan&lat=40.0019640690812&lng=116.4869197104843&is_WiFi=1&channel_id=60&click_from=home HTTP/1.1'
    session_id = 'kpc82cl50hmtwf8allcvswtmqysnckpz'
    cookies = dict(sessionid=session_id)
    print(cookies)
    headers = {'user-agent': 'Gengmei/7.5.0 (iPhone; iOS 10.3.3; Scale/3.00)'}
    r = requests.get(url=url, cookies=cookies, headers=headers)
    print(r.cookies)
    return r


import time

for i in range(100):
    for ii in range(100):
        thread.start_new_thread(get, ())

    time.sleep(1)

print('done')
