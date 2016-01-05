# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 11:53:40 2016

@author: tzhang1
"""

import numpy as np

# This is create a portfolio class to feed in
# forecasting function

class Portfolio(object):
    def __init__(self, weight, assets, corr):
        self.weight = weight
        self.assets = assets
        self.corr = corr
        self.mean = np.array([])
        self.stdev = np.array([])
        self.skew = np.array([])
        self.kurt = np.array([])# Correlation is a matrix variable her
        for asset in self.assets:
            self.mean = np.append(self.mean, asset.mean)
            self.stdev = np.append(self.stdev, asset.stdev)
            self.skew = np.append(self.skew, asset.skew)
            self.kurt = np.append(self.kurt, asset.kurt)
            
        self.cov = self.corr * np.outer(self.stdev, self.stdev)      

        
        








