#!/usr/bin/env python
# coding=utf-8

### lambda 构建一些简单的  函数 快速使用 

def f(x,y):
    return x*y 
print f(2,3)

###equals

g=lambda x,y:x*y ### 生成函数对象
print g,g(2,3) ###g是lambda函数生成的匿名函数 

### reduce()
print reduce(f,range(1,6))
print reduce(lambda x,y:x+y, range(1,6))

### switch (no swtich in python, but can use dictionary)

def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

operater={'+':add,'-':minus,'*':multiply,'/':divide}
### operater can be easier like this: operater={'+':x+y,'-':x-y........}   operater.get('+-*/')  done~

def oper(x,y,o):
    return  operater.get(o)(x,y)

print oper(2,4,'*')

### useful inner funnction

a=35
print bin(a)### binary
print hex(a)### 16
print oct(a)### 10
print chr(a) ### char->ascii
print ord(chr(a))###ascii->char

### about string

s="hello my darling"
print s.capitalize()
print s.replace('l','R',2)### new,old 2times   replace l->R   first 2 l 
s='192.168.1.12'
print s.split('.',2) ### split by . into a list     -> .  2times

### about sequence

l=range(10)
def ff(x):
    if x>5:
        return True

print filter(ff,l)  ###将序列应用于函数(应该是参数,即先调用ff(l),在filter)，滤出返回值为True的值

### zip map  并行遍历

name=['mike','chen','else']
age=[22,33,44]
tel=['123','456','888']
tel2=['222','333']
print zip(name,age,tel)
print zip(name,age,tel,tel2) ### tel2 only has 2 elem  ,最后一个不同样长度的被丢弃了

print map(None,name,age,tel,tel2)  ###不足位用None填充

def mf(x,y,z):
    return x+y+z

a=[1,2,3]
b=[2,3,4]
c=[3,4,5]
print map(mf,a,b,c)   ###将abc进行并行遍历后再依次作为参数传给mf进行计算，返回计算结果



