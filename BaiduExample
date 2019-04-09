import requests
keyword = 'python'
try:
    kv = {'wd':keyword}
    r = requests.get('http://www.baidu.com/s', params = kv)
    print(r.request.url)  #返回url链接
    r.raise_for_status
    print(len(r.text))
except:
    print('Fail to crawl.')
