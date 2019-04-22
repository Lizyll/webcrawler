import re

#re默认greedy匹配，即输出匹配最长的子串
match = re.search(r'PY.*N', 'PYAMNMCMDN')
print(match.group(0))

#ungreedy匹配
match = re.search(r'PY.*?N', 'PYAMNMCMDN')
print(match.group(0))
