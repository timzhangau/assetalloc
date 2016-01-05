# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 11:53:40 2016

@author: tzhang1
"""

import numpy as np

# This is create a portfolio class to feed in
# forecasting function

class Portfolio(object):
    def __init__(self, weights, assets, corr):
        self.weights = weights # weights is a numpy array
        self.assets = assets
        self.corr = corr
        self.mean = np.array([])
        self.stdev = np.array([])
        self.skew = np.array([])
        self.kurt = np.array([]) # Correlation is a numpy array
        for asset in self.assets:
            self.mean = np.append(self.mean, asset.mean)
            self.stdev = np.append(self.stdev, asset.stdev)
            self.skew = np.append(self.skew, asset.skew)
            self.kurt = np.append(self.kurt, asset.kurt)
        
    def calculate_portfolio_stats(self):
        if np.sum(self.weights) == 1:
            self.mean = np.dot(self.weights, self.mean)
            self.stdev = np.dot(np.dot(self.weights, self.cov), self.weights)
        else:
            print 'Check Portfolio Weights, sum not equal to 100%'
            
            
        
    

        
        








