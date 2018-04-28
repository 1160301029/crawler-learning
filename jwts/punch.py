# http://210.46.72.143/student/studentInfo.jsp?userName=1161100101&passwd=

import requests
import json
from urllib.request import urlretrieve
import time

from bs4 import BeautifulSoup

baseurl = 'http://210.46.72.143/student/studentInfo.jsp?userName='
pwd = '&passwd='

# 这里的cookie可以通过chrome的F12请求一次拿到，请用你自己的
cookies = {
    "JSESSIONID": "EB2F955EFD4690C93C3B11FA86100D40",
}

xh = 1161000101

with open('10' + '.txt', 'a') as file:
    # 循环次数自己看着该
    for i in range(29):
        try:
            r = requests.get(baseurl+str(xh + i)+pwd+str(xh+i),cookies = cookies)
            soup = BeautifulSoup(r.text,"lxml")
            tables = soup.findAll('table')  #解析table
            tab = tables[4] #实践所得
            for tr in tab.findAll('tr')[1:9]:
                for td in tr.findAll('td'):
                    try:
                        file.write(td.getText().strip() + '  ')
                        print(td.getText().strip())
                    except Exception as e:
                        print('写入失败')
                file.write('\n')
            # print(tables[4])

        except Exception as e:
            print("error")
        file.write('\n')
        print('\n')
        time.sleep(2)

