import requests
import json
from urllib.request import urlretrieve
import time

urllist = []
baseurl = "http://complab.baicizhan.com/images/"
for times in range(36):
    url = "http://complab.baicizhan.com/wallpaper/papers/more_paper"
    post_data = {
        "time": str(times),
        "tab": "1"
    }
    # Get Cookie
    cookies = {
        "_wall_session": "SXJGZmlPVTdGRnpRVC8zSkR2V3RYMndxalJxbzFVTkhvN3NxUXNackNETk9keVduaGRBSSsxd2c4ZTZudzFZLzROTFBYL0VmSldNU0lHbUlHY3h4TmdjTmJCUXQzeHpLQmlzcVpDRFhqV1dLN3E1dnFDQzJ1YzZsVUNjZTBrN3QrMkgveGhCci9ib3k1RVhPUGM0U2lRPT0tLXZHczlYWHZWZFlXaDRpdzhPdnpCR2c9PQ%3D%3D--84b322f67df0b7a97d14bb1431f85d92b7271fce"
    }

    # Set Headers
    headers = {
        "X-CSRF-Token": "CKZuqFsTm/TFOiIkzJjFKb026rbbNWjMRDDyeDgIHx0="
    }

    # Send Post requests
    try:
        r = requests.post(url, data=post_data, cookies=cookies, headers=headers)
        rjson = json.loads(r.text)
        print(r.text)
        rdata = rjson['data']
        for imgdata in rdata:
            #print(imgdata['url'])
            urllist.append(imgdata['english'] + "#" + baseurl + imgdata['url'])
        print(times + 1, "/ 36")
    except Exception as e:
        print(str(times) + "error")


i = 0
for url in urllist:
    print(url)
    try:
        urlretrieve(url.split("#")[1], "img/" + url.split("#")[0] + ".jpg")
        i = i + 1
    except Exception as e:
        print("error: "+ url.split("#")[0] , e)
    except IOError as e:
        print("file error: "+ url.split("#")[0] , e)