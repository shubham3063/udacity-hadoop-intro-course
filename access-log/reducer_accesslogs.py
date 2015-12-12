#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:05:47 2015

@author: hduser
"""

import sys

#mode = 'hits2page'
#mode = 'hitsbyip'
mode = 'popularfile'

def part2_hits2page():
    prev = ''
    total = 0
    for line in sys.stdin:
        # remove trailing and leading whitespaces
        line = line.strip()
        
        # split the line using tab
        key,val = line.split('\t')
        
        val = float(val)    

        if key == prev:
            total += val
            
        elif key != prev:
            if prev:
                print "%s\t%s" % (prev,total)
            total = val
            
        prev = key
    
    print "%s\t%s" % (prev,total)

def part2_popularfile():
    prev = ''
    total = 0
    globalmax = -1
    globalfile = ''
    for line in sys.stdin:
        try:
            # remove trailing and leading whitespaces
            line = line.strip()
            
            # split the line using tab
            key,val = line.split('\t')
            
            val = float(val)
    
            if key == prev:
                total += val
                
            elif key != prev:
    #            if prev:
    #                print "%s\t%s" % (prev,total)
                if total > globalmax:
                    globalmax = total
                    globalfile = prev
                total = val
                
            prev = key
        except:
            continue
    
    print "%s\t%d" % (globalfile,globalmax)
    
if mode == 'hits2page' or mode == 'hitsbyip':
    part2_hits2page()
    
elif mode == 'popularfile':
    part2_popularfile()

