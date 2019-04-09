import requests
import os

url = input('Enter a url: ')
root = 'D://pics//'
path = root + url.split('/')[-1]  #以‘/’分割的最后一部分，即jpg文件
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('pic saved.')
    else:
        print('the file has already existed.')
except:
    print('Fail.')
