from bs4 import BeautifulSoup
import requests
import re

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.find_all(['a', 'b']))  #a,b标签以list的形式找出
for tag in soup.find_all(True):  #True：所有标签
    print(tag)
for tag in soup.find_all(re.compile('b')):  #正则表达式以b开头的所有信息作为查找的要素
    print(tag.name)
print(soup.find_all('p', 'course'))
print(soup.find_all(id='link1'))  #对属性进行绝对查找
print(soup.find_all(id=re.compile('link')))  #正则表达式，不需要精确到link1，只需要一部分就可以查找
print(soup.find_all('a', recursive=False))  #[]说明a根节点没有标签，子孙节点才有
print(soup.find_all(string = 'Basic Python'))
print(soup.find_all(string = re.compile('python')))  #字符串中所有出现python的检索出来
for link in soup.find_all('a'):
    print(link.get('href'))
