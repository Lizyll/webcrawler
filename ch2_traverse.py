import requests
from bs4 import BeautifulSoup
r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
#标签树的下行遍历
for child in soup.body.children:  #遍历子孙节点
    print(child)

#标签树的上行遍历
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#标签树的平行遍历
for sibling in soup.a.next_siblings: #遍历后续节点
    print(sibling)
for sibling in soup.a.previous_siblings: #遍历前序节点
    print(sibling)
