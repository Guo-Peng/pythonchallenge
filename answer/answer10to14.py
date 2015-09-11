# coding:utf-8
# pythonchallenge.com
# http://www.pythonchallenge.com/pc/def/map.html 不断改变最后的部分来进行下一关的跳转


# 10.根据规律算出a 进而算出len(a[30]) a = [1, 11, 21, 1211, 111221
# 后一个数是对前一个数的描述
# 正则反向引用！
import re

a = '1'
# for x in range(30):
#     a = ''.join([str(len(i + j)) + i for i, j in re.findall(r'(\d)(\1*)', a)])
# print len(a)

for x in range(30):
    split = re.findall(r'(\d)', a)
    word = split[0]
    p = 0
    num = 0
    result = ''
    for y in split:
        if y == word:
            num += 1
        else:
            result += str(num) + word
            word = y
            num = 1
        if p == len(split) - 1:
            result += str(num) + word
            a = result
        else:
            p += 1
print len(a)


# http://www.pythonchallenge.com/pc/return/5808.html
# 11.像素操作      将奇偶像素分开分别组成图片
from PIL import Image, ImageDraw

pic = Image.open('/Users/Peterkwok/GitHub/pythonchallenge/cave.jpg')
w, h = pic.size
odd = even = Image.new(pic.mode, (w / 2, h / 2))
for x in range(w):
    for y in range(h):
        pixel = pic.getpixel((x, y))
        if (x + y) % 2 == 0:
            even.putpixel((x / 2, y / 2), pixel)
        else:
            odd.putpixel((x / 2, y / 2), pixel)
odd.save('/Users/Peterkwok/GitHub/pythonchallenge/odd.jpg')
even.save('/Users/Peterkwok/GitHub/pythonchallenge/even.jpg')


# 12.根据发牌的提示将文件分为5分 得到5个图片
source = open('/Users/Peterkwok/GitHub/pythonchallenge/evil2.gfx', 'rb')
content = source.read()
source.close()
for x in xrange(5):
    result = open('/Users/Peterkwok/GitHub/pythonchallenge/evil_%d.png' % x, 'wb')
    result.write(content[x::5])
    result.close()


# 13.利用xmlrpclib 调用远程服务器的函数，根据之前的提示Bert
import xmlrpclib

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server.system.listMethods()
print server.system.methodHelp('phone')
print server.phone('Bert')
# http://www.pythonchallenge.com/pc/return/italy.html


# 14.面包提示按照面包的纹理进行卷，根据10000的分组以及图片的尺寸来确定将图片的像素按照面包的纹理进行重新排列
# 将像素按照方向内卷的方式重新排列
from PIL import Image

pic = Image.open('/Users/Peterkwok/GitHub/pythonchallenge/wire.png')
w = h = 99
total = 0
tan = 0
result = Image.new(pic.mode, (w + 1, h + 1))
list = []
for x in xrange(100, 1, -2):
    list.append(x)
    list.append(x - 1)
    list.append(x - 1)
    list.append(x - 2)
for x in list:
    if tan % 4 == 0:
        h += 1
        for y in xrange(x):
            pixel = pic.getpixel((y + total, 0))
            h -= 1
            result.putpixel((w, h), pixel)
        total += x
    elif tan % 4 == 1:
        w += 1
        for y in xrange(x):
            pixel = pic.getpixel((total + y, 0))
            w -= 1
            result.putpixel((w, h), pixel)
        total += x
    elif tan % 4 == 2:
        h -= 1
        for y in xrange(x):
            pixel = pic.getpixel((total + y, 0))
            h += 1
            result.putpixel((w, h), pixel)
        total += x
    else:
        w -= 1
        for y in xrange(x):
            pixel = pic.getpixel((total + y, 0))
            w += 1
            result.putpixel((w, h), pixel)
        total += x
    tan += 1
result = result.transpose(Image.ROTATE_90)
result.show()
result.save('/Users/Peterkwok/GitHub/pythonchallenge/challenge_14.png')
pic.close()
# http://www.pythonchallenge.com/pc/return/uzi.html


