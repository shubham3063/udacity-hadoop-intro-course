#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:41:19 2015

@author: hduser
"""

import sys

#mode = 'hits2page'
#mode = 'hitsbyip'
mode = 'popularfile'

def part2_hits2page(line):
    return line.split()[6]
    
def part2_hitsbyip(line):
    return line.split()[0]

def part2_popularfile(line):
    path = ''
    path = line.split()[6]
    if path.startswith('http://www.the-associates.co.uk'):
        path = path[31:]
    return path
    
# read input line by line from the standard input
for line in sys.stdin:
    try:
        # strip the line of leading and trailing whitespaces
        line = line.strip()
        key = ''
        val = 0
        if mode == 'hits2page':
            key = part2_hits2page(line)
            val = 1
        elif mode == 'hitsbyip':
            key = part2_hitsbyip(line)
            val = 1
        elif mode == 'popularfile':
            key = part2_popularfile(line)
            val = 1

    except:
        # leave the line and continue processing the next lines
        continue
    else:
        # print the data on the output stream
        print '%s\t%s' % (key,val)
