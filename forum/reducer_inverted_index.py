#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:59:41 2015

@author: hduser
"""

import sys

def getstr(ids):
    s = ''
    for i in ids:
        s += i + ','
    return s

prev = ''
ids = []
count = 0
#reader = csv.reader(sys.stdin,delimiter='\t')
for line in sys.stdin:    
    word,nodeid = line.strip().split('\t')
#    print ids
    if word == prev:
        ids.append(nodeid)
    else:
        if prev!='':
            ids.append(str(count))
            print "%s\t%s" % (prev,getstr(ids))
        ids = []
        ids.append(nodeid)
        count = 0
    prev = word
    count += 1
ids.append(str(count))
print "%s %s" % (prev,getstr(ids))