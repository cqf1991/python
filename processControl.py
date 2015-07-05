#!/usr/bin/env python
# coding=utf-8
### if control

if 1<2: 
    ### always use 4 blanks 
    print 'ok'
    print 'abc'

if 1>2:
    print 'ok'
elif 2>1:
    print 'elif'
else:
    print 'not ok'
print 'out of if control'


if 2>1:
    if 3>1:
        print 'in 2 if '

### and  or  not 

x=int(raw_input('input x'))  ### must int() otherwise x will be init as str

print x,type(x)
if x>10 and x<20:
    print 'x>10&&x<20'
elif x<10 or x>20:
    print 'x<10 or x>20'
else:
    print x

print not True

### following is about for

for x in 'abcd':
    print x,"runs"

for x in [1,2,3]: ### x is var , after in is sequence(str tuple dictionary)
    print x


print range(1,11,2) ### range()->  [start,end),step

print xrange(10) ### xrange() return an iter object

l=[1,2,3,4,'a','b']
for x in l:
    if x>2:
        print x

d={1:111,2:222,5:555,4:444,3:333} ### dic has no order 

for x in d:
    print x ### x prints key 
    print d[x]

for  x in d.values():
    print x
    

for k,v in d.items():
    print k,'+',v
else:
    print 'end'

for x in range(1,11):
    print x
    if x==6:
        break
else:
    print "end"   ### the for has been break  won't print end

for x in range(1,11):
    print x
    if x==3:
        pass  ### do nothing  but must have this statement  代码桩，占位 不可省略
    if x==2:
        print 'this is x=2'
        continue ### won't run print '#'
    if x==6:
        break
    print '#'*50
else:
    print "end"

### while is the same 



