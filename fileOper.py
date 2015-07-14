#!/usr/bin/env python
# coding=utf-8

### about file system

fo=open('fileOper.txt')
print 'before oper read:',fo.read()
fo.close()

### w/w+=write and read(del source and create new)
### r/r+=read and write
fo=open('fileOper.txt','w+') ### del source file and then write in to file   && can used for create a new file
fo.write('new data2222')  ### write in to buffer
print fo.read()  ### wrong read,  data is in buffer not in file
fo.close()  ### write in to file



fo=open('fileOper.txt','r+')
fo.write('NNN') ### replace 'new',write in the start position
fo.read() ###let the file pointer point to the last position of the file 
fo.write('ccccc')
print fo.read()### wrong read, data is in buffer too
fo.close()


fo=open('fileOper.txt')
print 'after oper read:',fo.read()
fo.close()


### file lesson 2  about read

fo2=open('fileOper2.txt','w+')
fo2.write(''' first line
         second line
         third line  hahaha love~ ''')
fo2.close() ### write in file

fo2=open('fileOper2.txt') ### new data is in file 

print fo2.readline() ### file must be open // readline(size)  size Is num of char
### readline or readlines operation will change the index, so you can find that next readlines has 2 elem in lists
print fo2.readlines() ### return a list   ,index at the second line 
print fo2.readline() ###  return null str
###print fo2.next() ### print warning ,has no elem

fo2.close()


### about write  flush   seek(offset,options(0:start,1:current,2:end))

fo2=open('fileOper2.txt','a+')
ls=['\none\n','two\n','three\n']
fo2.writelines(ls)
fo2.flush()### write buffer to file
print fo2.readlines() ### pointer  at the end,print null
fo2.seek(0,0)### let the pointer point to the position 0(start), offset 0(-/+/0 is ok)
print fo2.readlines()### print list all lines
fo2.close()



