import requests
url = input('Enter a url: ')
try:
    r = requests.get(url)
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)  #修改headers字段模拟浏览器发出请求
    print(r.status_code)
    print(r.request.headers)
    print(r.text[1000:2000])
except:
    print('Fail to crawl.')
