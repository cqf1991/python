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


### file lesson 2

fo.open('fileOper.txt','w+')
fo.write('''
         first line
         second line
         third line  hahaha love~
         ''')
fo.close()




