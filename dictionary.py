#!/usr/bin/env python
# coding=utf-8

### following is about python dictionary  like hash,changable,non-ordered
### dic={key:value}

dic={'a':0,'b':1,'c':3}
print(dic['a'])### str also an object, can not get value by index, need the key ~

name='456'### must be init the var 
dic2={1:'123','a':'mile',name:123}
print dic2
print(dic2['456'])

for k in dic2:
    print dic2[k]

### add in dictionary  but no order

dic2['new']='newvalue'###add
print dic2

dic2['new']='change'###change
print dic2

###del

dic2.pop('new') ###return & del
print dic2

dic.clear() ### del all elems
print dic

del(dic)


###  print dic  will be wrong  dic has been deleted




print dic2.keys()
print dic2.values()
