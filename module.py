#!/usr/bin/env python
# coding=utf-8


### python module and package

import function_2 as f

###print '外部调用:',function_2.tel2

print '外部调用:',f.tel2

from function_2 import add   #引用制定函数，调用是无需前缀

print 'add',add(1,2)

import pyPackage.function   ###调用包，将文件夹建立一个__init__.py文件  即可声明该文件夹为包


