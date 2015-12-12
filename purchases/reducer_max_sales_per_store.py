#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:30:33 2015

@author: hduser
"""

import sys
prev = ''
maxcost = 0
for line in sys.stdin:
    # remove trailing and leading whitespaces
    line = line.strip()
    
    # split the line using tab
    store,cost = line.split('\t')
    
    # convert the cost to float
    cost = float(cost)    
    
    # if current store name is same as the last store name
    # get the maximum value of the current cost and maximum cost so far
    if store == prev:
        maxcost = max(maxcost,cost)
        
    # if the store name is not same as the last store name
    # print the max cost so far for the last store (if it is not the first store)
    # assign the current cost of the new store to the max cost so far
    elif store != prev:
        if prev:
            print "%s\t%s" % (prev,maxcost)
        maxcost = cost
        
    # store the current store name as the last/previous store name
    prev = store

# print the max cost so far of the last store that was not printed in the for loop
print "%s\t%s" % (prev,maxcost)

