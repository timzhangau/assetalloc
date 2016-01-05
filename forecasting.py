# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 14:12:48 2016

@author: tzhang1
"""

# This is to create Forecasting function to calculate
# portfolio risk and return profile

import numpy as np
from assetalloc.portfolio import Portfolio
from assetalloc.asset import Asset

class Forecasting(object):
    
    def __init__(self, portfolio, method, simulations, 
                 balance, percentile, projectyear):
        self.portfolio = portfolio
        self.method = method
        self.simulations = 2000
        self.balance = 100000
        self.percentile = 0.05
        self.projectyear = [1, 5, 10]
        self.mean = np.array([])
        self.stdev = np.array([])
        self.skew = np.array([])
        self.kurt = np.array([])
        for asset in portfolio.assets:
            self.mean = np.append(self.mean, asset.mean)
            self.stdev = np.append(self.stdev, asset.stdev)
            self.skew = np.append(self.skew, asset.skew)
            self.kurt = np.append(self.kurt, asset.kurt)
            
        self.cov = portfolio.corr * np.outer(self.stdev, self.stdev)
        
     def return_range
        
        
        