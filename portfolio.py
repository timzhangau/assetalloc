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
        self.corr = corr # Correlation is a numpy array
        self.a_rtn_ls = np.array([])
        self.g_rtn_ls = np.array([])
        self.stdev = np.array([])
        self.skew = np.array([])
        self.kurt = np.array([])
        for asset in self.assets:
            self.a_rtn_ls = np.append(self.a_rtn, asset.a_rtn)
            self.g_rtn_ls = np.append(self.g_rtn, asset.g_rtn)
            self.stdev_ls = np.append(self.stdev, asset.stdev)
            self.skew_ls = np.append(self.skew, asset.skew)
            self.kurt_ls = np.append(self.kurt, asset.kurt)

"""
Methods need to be built for Portfolio object:
    - Calculate portfolio metrics
    - Portfolio Optimization
    - Portfolio Forecasting
"""
    

    
    def calculate_portfolio_stats(self):
        if np.sum(self.weights) == 1:
            self.a_rtn = np.dot(self.weights, self.a_rtn_ls)
            self.g_rtn = np.dot(self.weights, self.g_rtn_ls)
            self.cov = self.corr * np.outer(self.stdev_ls, self.stdev_ls)
            self.stdev = np.dot(np.dot(self.weights, self.cov), self.weights)
            self.g_rtn = (1 + self.a_rtn) * 
            exp(-0.5 * (self.stdev**2) * ((1+self.a_rtn)**-2)) -1
        else:
            print 'Check Portfolio Weights, sum not equal to 100%'
            
            
        
    

        
        








