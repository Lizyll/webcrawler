import requests
keyword = 'python'

try:
    kv = {'q':keyword}
    r = requests.get('http://www.so.com/s', params = kv)
    r.raise_for_status
    print(r.request.url)
    print(len(r.text))
except:
    print('Fail.')
