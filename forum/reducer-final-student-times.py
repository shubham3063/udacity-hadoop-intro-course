#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:29:45 2015

@author: hduser
"""
import sys
import numpy as np
prev = ''
hours = [0]*24

for line in sys.stdin:

    line = line.strip()
    
    user,hr = line.split('\t')   
    
    if prev and user != prev:
        maxhours = np.argwhere(hours == np.amax(hours))
        maxhours = maxhours.flatten().tolist()
        for mh in maxhours:        
            print "%s\t%s" % (user,mh)
        hours = [0]*24
        
    hr = int(hr)
    hours[hr] += 1       

    prev = user    
    
print "%s\t%s" % (prev,np.argmax(hours))
    