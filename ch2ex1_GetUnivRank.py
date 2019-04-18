import requests
from bs4 import BeautifulSoup
import bs4

#从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Fail'

#提取网页内容中信息到合适的数据结构
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:  #解析tbody标签所在位置
        if isinstance(tr, bs4.element.Tag):  #tbody中找到每所大学对应的tr标签，过滤掉非标签信息
            tds = tr('td')  #在tr标签中找到td标签的信息，把需要的td标签存入列表
            ulist.append( [tds[0].string, tds[1].string, tds[2].string] )

#利用数据结构展示并输出结果
def printUnivList(ulist, num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名', '学校', '总分'))
    for i in range (num):
        u = ulist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0], u[1], u[2]))

if __name__ == '__main__':
    unifo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)  #20 univs
