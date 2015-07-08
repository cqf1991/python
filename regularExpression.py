#!/usr/bin/env python
# coding=utf-8


###regular expression 


import re  ###正则表达式处理模块

s='abc'

s=r'abc'  ###定义s的rule 

print re.findall(s,'abcabcabccdasdfabcasdfabcbasdbabc')

s=r'fabcas' ### new rule


print re.findall(s,'abcabcabccdasdfabcasdfabcbasdbabc')

### -----------------

st= 'top tip tqp twp tep'

res=r't[io]p' ###使用正则方式

print re.findall(res,st)

st='top tap top tsp'
res=r'^top'  ###匹配行首时 ^放在前面 ^top
res2=r'tsp$' ###匹配行尾时 $放在后面 tsp$
print re.findall(res,st)
print re.findall(res2,st)

res=r't[^o]' ###匹配ta  ts  即 t除了o都可以，只有放首位才有此意义  r't[o^] 表示匹配to或者t^
print re.findall(res,st)

st='x1x x2x'
res=r'x[0-9A-Za-z]'
print re.findall(res,st)

###  \^ 　转义同样适用

r=r'\^abc'
print re.findall(r,'^abc')

###\w=[a-zA-Z0-9]    \W[^a-zA-Z0-9]

r=r'^025-[0-9]{8}'###[0-9]{8}　８次  {m,n}至少重复Ｍ次，至多重复ｎ次，　　　　[0-9]* 0次到多次，　　　[0-9]+  1次到多次 　　， [0-9]? ０次到１次
print re.findall(r,'025-84089436')

r=r'ab+?'###非贪婪模式　　只取一个ｂ
print re.findall(r,'abbbbbbbbbbb')

###-----------------------------------functions in regular


r=re.compile(r'abcd',re.I) ###re.I忽视大小写
print r.findall('aBCd')
print r.match('bbcdabcd') ###匹配成功时返回ｍａｔｃｈ对象，否则返回空，但是只匹配开头
print r.search('babaabcd') ### search 可以匹配在开头和结尾的ａｂｃｄ，

x=r.finditer('abcdbdfababcdabcdsdfsabcd')

print x.next()

###正则替换字符串

rs=r'c..t'
print re.sub(rs,'python','qwepoi cdst sdlkf cqqt sdkfj cvst') ###cdst cqqt cvst  ->python

### 正则切割字符串～nice

rs=r'[\+\-\*\/]'
print re.split(rs,'123+456-444*777/666')

###　数据多行的问题

s="""
hello abc
cda hello
u never know
haha
"""

r=r'^hello'
print re.findall(r,s) ### bad  因为开头有/n　通过ｒｅ.M处理
print re.findall(r,s,re.M)

email=r'\w{3}@\w+(\.com|\.cn)'
print re.findall(email,'abc@aaa.cn')## 用()分组后　优先返回分组当中的数据，用ｍａｔｃｈ可以确定是否ｍａｔｃｈ

### example
s="""
hhsdj  dskj   hello src=csvt yes  jdjsds
djhsjk src=123 yes jdsa
src=234 yes hello src=python yes ksa
"""

r=r'hello src=(.+) yes'
print re.findall(r,s)






