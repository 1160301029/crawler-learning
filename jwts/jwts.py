import requests
import json
from urllib.request import urlretrieve
import time
import os

baseurl = 'http://jwts.hit.edu.cn/xswhxx/showPhoto?xh='

# 这里的cookie可以通过chrome的F12请求一次拿到，请用你自己的
cookies = {
    "JSESSIONID": "7fCLhJFR2PRTvkNvsZhjJ2JQnSt3fygXgrZxrBjS1xXMrC7ZvsJh!1543037378",
    "clwz_blc_pst": "150999212.24859"
}

grade = 116
xi = 100


# 循环次数自己看着该
for iclass in range(8,9):
    path = str(xi).zfill(3) + '/'+ str(iclass)
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(21,30):
        xh = str(grade) + str(xi).zfill(3) + str(iclass).zfill(2) + str(i).zfill(2)
        try:
            # r = requests.get(baseurl + str(xh + i),cookies = cookies)
            r = requests.get(baseurl + xh, cookies=cookies)
            try:
                with open(path + '/'+xh + '.jpg', 'wb') as file:
                    file.write(r.content)
                    print(xh + ' complete')
            except Exception as e:
                print('写入失败')
        except Exception as e:
            print(str(xh) + "error")

        time.sleep(2)

