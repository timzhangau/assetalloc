# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 14:12:48 2016

@author: tzhang1
"""

# This is to create Forecasting function to calculate
# portfolio risk and return profile

from assetalloc.portfolio import Portfolio
from assetalloc.asset import Asset

class Forecasting(object):
    
    def __init__(self, portfolio, method, simulations, 
                 initialbal, percentile, projectyear):
        self.portfolio = portfolio
        self.method = method
        self.simulations = 2000
        self.initialbal = 100000
        self.percentile = 0.05
        self.projectyear = [1, 5, 10]
     
     def return_range
        
        
        