#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:30:33 2015

@author: hduser
"""

import sys
prev = ''
total = 0
for line in sys.stdin:
    # remove trailing and leading whitespaces
    line = line.strip()
    
    # split the line using tab
    store,cost = line.split('\t')
    
    # convert the cost to float
    cost = float(cost)    
    
    # if current store name is same as the last store name
    # add the cost to the running total
    if store == prev:
        total += cost
        
    # if the store name is not same as the last store name
    # print the total for the last store if it is not the first store
    # start a new running total with the current store
    elif store != prev:
        if prev:
            print "%s\t%s" % (prev,total)
        total = cost
        
    # store the current store name as the last/previous store name
    prev = store

# print the running total of the last store that was not printed in the for loop
print "%s\t%s" % (prev,total)

