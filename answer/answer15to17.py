# coding:utf-8
# pythonchallenge.com
# http://www.pythonchallenge.com/pc/def/map.html 不断改变最后的部分来进行下一关的跳转


# 15.通过观察该年为闰月 1月26日为周一 判断出符合的年份 然后选出倒数第二个 查看1756-1-27发生的事情   Mozart
# 根据1**6年来确定循环的年的范围
import datetime


def isleap(year):
    nextday = datetime.date(year, 3, 1)
    return (nextday - datetime.timedelta(1)).day == 29


for x in xrange(1006, 2000, 10):
    if isleap(x):
        day = datetime.date(x, 1, 26)
        if day.weekday() == 0:
            print str(x) + '-1-27'
# http://www.pythonchallenge.com/pc/return/mozart.html


# 16.每行都有5个品红的像素，将每行的品红像素移至最左端
from PIL import Image

pic = Image.open('/Users/Peterkwok/GitHub/pythonchallenge/picture/mozart.gif')
result = Image.new(pic.mode, pic.size)
init = 0
for row in xrange(480):
    for line in xrange(640):
        pixel = pic.getpixel((line, row))
        if pixel == 195:
            init = line
            break
    for line in xrange(640):
        result.putpixel((line, row), pic.getpixel(((line + init) % 640, row)))
    pixel = 0
result.show()
result.save('/Users/Peterkwok/GitHub/pythonchallenge/picture/challenge_16.gif')
# http://www.pythonchallenge.com/pc/return/romance.html


# 17.不断迭代网页，将cookie中隐藏的信息拿出来并经过url解码后进行拼接
import urllib2
import urllib
import re
import cookielib
import bz2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
result = []


def request(num):
    furl = url + num
    data = opener.open(furl).read()
    m = re.match('.*?the next busynothing is (\d+).*?', data)
    for cj in cookie:
        result.append(urllib.unquote_plus(cj.value))
    if m:
        print num
        return request(m.group(1))
    else:
        print num
        return num


mid = request('12345')
message = ''.join(result)
print bz2.decompress(message)

# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
# 莫扎特的父亲：Leopold ，通过13关的方法找到其号码

import xmlrpclib

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server.system.listMethods()
print server.system.methodHelp('phone')
print server.phone('Leopold')

# 得到VIOLIN

# 两种添加header的方法

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
headers = {'Cookie': 'info=' + urllib.quote_plus('the flowers are on their way')}
req = urllib2.Request(url, None, headers)
# req.add_header('Cookie', 'info=' + urllib.quote_plus('the flowers are on their way'))
print urllib2.urlopen(req).read()

# 得到返回信息 oh well, don't you dare to forget the balloons.

# http://www.pythonchallenge.com/pc/return/balloons.html
