#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:50:48 2015

@author: hduser
"""

import sys

totalcost = 0
totalsales = 0

for line in sys.stdin:
    # remove trailing and leading whitespaces
    line = line.strip()
    
    # split the line using tab
    key,cost = line.split('\t')
    
    # convert the cost to float
    cost = float(cost)    
    
    # total cost and sales    
    totalcost += cost
    totalsales += 1
    
# print the total cost and total sales
print "%s\t%s" % (totalcost,totalsales)

