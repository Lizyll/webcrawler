import requests
url = 'http://m.ip138.com/ip.asp?ip='
url1 = input('Enter a url: ')
try:
    r = requests.get(url + url1)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('Fail.')

#BIT:202.204.80.112
#BJFU 202.204.112.87
