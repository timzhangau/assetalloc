# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 15:40:32 2016

@author: tzhang1
"""

# This is to create an Asset class to store risk and 
# return attributes

class Asset(object):
    def __init__(self, mean, stdev, skew, kurt):
        self.mean = mean
        self.stdev = stdev
        self.skew = skew
        self.kurt = kurt