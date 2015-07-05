#!/usr/bin/env python
# coding=utf-8

str1="abc"
print(str1*5)
print('c' in str1)



print(max(str1))

str2="123"

print(cmp(str1,str2))
print(cmp(str2,str1))

str1="123"
print(cmp(str1,str2))

### up is strings, down is tuple

t=('mike',24,'boy')
print(t)
print(t[1],t[2])
t2=(2)
t3=(2,)
print('123',t2,t3,type(t2),type(t3))

name,age,sex=t ### always use in this way

### t[1]=25  is wrong

###up is tuple  down is list

l=['mike',24,'boy',t]
print(l[0],l[3],l[3][1])
l[0]='mikechen'
print(l[0],l[3],l[3][1])
### list can be changed following is about add sth to list

### l[4] is wrong because u init with l[3] so u must to append a space 

l.append('end')
print(l[4])

### remove sth in list 

print("remove")
print(l)

l.remove('end') ### can remove certain value
l.remove(l[0]) ### can remove by index 
del(l[0])
print(l[0],'---',l)



