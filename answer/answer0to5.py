# coding:utf-8
# pythonchallenge.com
# http://www.pythonchallenge.com/pc/def/map.html 不断改变最后的部分来进行下一关的跳转


# 0. 指数特性
print 2**38


# 1. 字符移位
def trans(s):
    num = ord(s)
    if (num >= 97) and (num <= 122):
        return chr(num + 2) if num + 2 <= 122 else chr(num + 2 - 26)
    return s


# word = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc ' \
#        'dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr ' \
#        'gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
word = 'map'
result = ''
for x in map(trans, word):
    result += x
print result.replace('\"', ' ').replace('. ', '.\n')


# 2.源码中找最少的字符 保证顺序才能得到正确结果
import string
import collections


def choose(s):
    if s in string.ascii_lowercase:
        return s
    return ''


f = open('data', 'r')
data = f.read()
result = collections.OrderedDict()
for x in data:
    if x in result:
        result[x] += 1
    else:
        result[x] = 1
count = [(value, key) for key, value in result.items() if value == 1]
print count
f.close()


# 3.一个小写字母左右均为3个大写字母
import re

f = open('data', 'r').read()
word = f.replace('\n', '')
m = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', word)
result = ''
for x in m:
    result += x
print result


# 4.不断请求页面获取5位数字进行迭代
import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


def request(num):
    furl = url + num
    data = urllib2.urlopen(furl).read()
    m = re.match('.*?(\d+).*?', data)
    if (m):
        print num
        return request(m.group(1))
    else:
        print num
        return num


mid = request('12345')
print 'next'
request(str(int(mid)/2))
request('63579')


# 5.读 peak hell - > pickle  包用于保存对象到文件中
import pickle

file = open('banner.p', 'r')
data = pickle.load(file)
for line in data:
    result = ''
    for word in line:
        num = word[1]
        for x in range(num):
            result += word[0]
    print result
