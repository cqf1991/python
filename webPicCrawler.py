#!/usr/bin/env python
# coding=utf-8

###python web  picture  crawler
import re
import urllib

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src=\"(http:\/\/imgsrc.+?\.jpg)\" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for i in imglist:
        urllib.urlretrieve(i,'%s.jpg' % x)
        x+=1

html=getHtml('http://tieba.baidu.com/p/3883238659')

print getImg(html)


