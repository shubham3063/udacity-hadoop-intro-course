#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:05:30 2015

@author: hduser
"""
import sys,re,csv

reader = csv.reader(sys.stdin,delimiter='\t')
reader.next()
p = re.compile(ur'[^\s+\,\.\!\?\:\;\"\(\)\<\>\#\$\=\-\/]+')
try:
    for line in reader:
        try:
            if len(line)>=5:
                nodeid = line[0]
                body = line[4]
                if not body or not nodeid:
                    continue
                words = [w.lower() for w in re.findall(p,body)]
                for w in words:
                    print "%s\t%s" % (w,nodeid)
        except:
            continue
except:
    pass
#    else:
#        for w in words:
#            print "%s\t%s" % (w,nodeid)


