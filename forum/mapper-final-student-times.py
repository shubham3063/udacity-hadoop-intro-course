#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:19:47 2015

@author: hduser
"""


import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    
    user = line[3]
    time = line[8].split()[1]
    time = time.split(':')[0]
    print "%s\t%s" % (user,time)    
