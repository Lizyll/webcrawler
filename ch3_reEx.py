import re

###函数式用法###
#re.search(pattern, string, flag)
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

#如果需要用到返回的值需要先用if判断是否为空，否则易报错
#match 从一个字符串开始位置起匹配正则表达式，返回match对象
#re.match(pattern, string, flags=0)
match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
    print(match.group(0))

#findall(pattern, string, flags=0) 返回list
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)

#re.split(pattern, string, maxsplit=0, flags=0)将字符串按照re匹配结果进行分割，返回list  
print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084'))
#maxsplip最大分成多少份,剩下的部分整体输出，不再切分
print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1))

#re.finditer(pattern,string, flags=0) 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))

#re.sub(pattern, repl, string, count=0, flags=0)替换匹配的正则表达式子串，返回替换后的字符串，repl要替换的string，count匹配的最大替换次数
print(re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084'))

###面向对象用法###编译后多次操作
#regex = re.compile(pattern, flags=0) 将正则表达式的字符串形式编译成正则表达式对象
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('BIT 100081')
print(rst)
