#!/usr/bin/env python
# coding=utf-8

### chapter 4  function 

a=1
b=2
def add(c,p=3333333):  ### 形参可以赋默认值, 传值时默认值无效，使用传过来的
    x=a+b+c+p          ### 默认参数放在右边，不然会出问题，例如  add(c=3,a) 这时a无法传参
    print c,'+',x,p
    global b
    b=500
    
add(122)
add(123,234)

print b
###  print x  wrong,x in add()

def add2():
    return 'add2 function'   ### just return it 
print add2()

###  多类型传值 列表，元祖，字典

def f(x):
    print x

dic={1:2,2:3}
l=range(10)
tp=('a','b')

f(dic)
f(l)
f(tp)

### important

def f2(x,y):
    print x,':',y

f2(*tp) ### 一一对应可以传值
f2(x=123,y=456)  ### 带参数的名字进行传值是OK的
### f2(*l)  ### 长度不对应不可
l=range(2)### l->list[2]   ok
f2(*l)

### fun->dictionary

def f3(name,age):
    print name,'+',age

dic2={'name':'mike','age':23}

f3(**dic2) ### OK  参数列表要对应字典的 key 即可传值
f3(name='free',age=45)  ###这样传也要对应字典的Key
f3(dic[1],dic[2])  ### dic和dic2不同，这样可以按值传递

###处理多余参数->变成元组

def f4(x,*p):  ###以元祖方式存储冗余
    print x
    print p  ###p is a tuple 接收冗余

f4('OK')
f4('this is x',123,456,789,101010)

def f5(x,*p,**pp): ###以字典方式存储冗余
    print x
    print p
    print pp

f5('OK')
f5('is x',2,3,4,5,y=20,z=30)   ### is x ->x   2,3,4,5->p   y=20 z=30 ->pp











