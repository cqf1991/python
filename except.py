#!/usr/bin/env python
# coding=utf-8


# try:  except XXError,msg:


try:
    open('abc.txt')
except IOError,msg:
    print msg
