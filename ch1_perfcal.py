import requests
import time

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Fail.'
if __name__ == '__main__':
    url = input('Enter a url: ')
    st = time.perf_counter()  #返回性能计数器的值，第一次的值
    for i in range (100):
        getHTMLText(url)
    dur = time.perf_counter() - st  #爬取100次后，减去第一次的值
    print('{:.2f}s'.format(dur))
