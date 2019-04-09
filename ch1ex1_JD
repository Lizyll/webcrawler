import requests
url = input('Enter a url: ')
try:
    r = requests.get(url)
    r.raise_for_status  #只有异常的时候才会抛出否则不运行
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('Fail to crawl.')
