#!/usr/bin/env python
# coding=utf-8



###python 浅拷贝 深拷贝

a=[1,2,3,'a','b']

b=a

print id(a)
print id(b)### same

a.append('d')
print a
print b  ### b will be changed because of a   

### a & b -> same memory

import copy

a=[1,2,3,['a','b','c']]

b=copy.copy(a) ### 浅拷贝，只拷贝父对象的内容

print id(a)
print id(b) ### copy -> not same memory

a.append('d')
print a
print b
### b won't change 

### 因为是浅拷贝  so  如下
print id(a[0])
print id(b[0]) ### same   子对象共享同一内存,这时改变可变类型的子元素的时候会跟着变

### 数字字符串是不可便类型，元祖列表是可变类型

a[3].append('d')

print a
print b ###跟着变，因为子对象占用的空间是一致的

### 深拷贝则是父对象和(可变类型)子对象都分别开辟内存存储

c=copy.deepcopy(a)

print a,'父对象memory:',id(a),'子对象(不可变类型)memory:',id(a[0]),'子对象(不可变类型(列表))memory:',id(a[3])

print c,'父对象memory:',id(c),'子对象(不可变类型)memory:',id(c[0]),'子对象(不可变类型(列表))memory:',id(c[3])




