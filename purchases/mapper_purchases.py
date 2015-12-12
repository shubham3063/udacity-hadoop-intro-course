#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:21:34 2015

@author: hduser
"""
# Sample input line
# 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex

import sys

# read input line by line from the standard input
for line in sys.stdin:

    try:
        # strip the line of leading and trailing whitespaces
        line = line.strip()
        
        # split the line into words with tab as delimiter
        line = line.split('\t')
        
        # the third and the fifth words are store name and cost of item repectively
        store = line[2]
        cost = line[4]
        
    except:
        # leave the line and continue processing the next lines
        continue
    else:
        # print the data on the output stream
        print '%s\t%s' % (store,cost)
