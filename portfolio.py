# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 11:53:40 2016

@author: tzhang1
"""

import numpy as np
from cvxopt import matrix, solvers

# This is create a portfolio class to feed in
# forecasting function

class Portfolio(object):
    def __init__(self, weights, assets, corr):
        self.weights = weights # weights is a numpy array
        self.assets = assets
        self.corr = corr # Correlation is a numpy array
        self.a_rtn_ls = np.array([])
        self.g_rtn_ls = np.array([])
        self.stdev_ls = np.array([])
        self.skew_ls = np.array([])
        self.kurt_ls = np.array([])
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
            self.a_rtn = np.dot(self.weights, self.a_rtn_ls)    # AR: Arithmetic Return
            self.g_rtn = np.dot(self.weights, self.g_rtn_ls)
            self.cov = self.corr * np.outer(self.stdev_ls, self.stdev_ls)
            self.stdev = np.dot(np.dot(self.weights, self.cov), self.weights)
            self.g_rtn = (1 + self.a_rtn) * 
            exp(-0.5 * (self.stdev**2) * ((1+self.a_rtn)**-2)) -1
        else:
            print 'Check Portfolio Weights, sum not equal to 100%'
            
            
        
"""
Portfolio Optimization
Methods:
    - Mean-Variance Optimization (MVO): traditional Harry Markowitz's MVO method. _
    It is a single-period optimization, only used to optimize AR and std dev.
    - MVO with Resampling: a combination of Monte Carlo simulation and conventional MVO. _
    Resample hypothetical return series through Monte Carlo and then calculate hypothetical set _
    of assumptions. Each set is optimized using MVO to form a set of asset mixes. All asset _
    mixes are grouped into bins by std dev and then averaged to produce one mix per std dev, _
    forming the resampled frontier. Still based on MVO, only available for AR and std dev.
    - Scenario-Based: Use a multivariate Monte Carlo simuation to create hypothetical/simulated_
    returns data for the parametric models of return distributions. Non-linear optimization _
    algorithm is then used to find the asset mixes at every level of reward that has the lowest _
    level of risk.

Return Distribution Assumptions:
    - Lognormal
    - Johnson: this account for skew and kurtosis
    - Bootstrapping: using historical series, account for non-linear co-variance

Optimization Objective:
    - Return:
        * Expected arithmetic mean return: single-period
        * Expected geometric mean return: multi-period
    - Risk:
        * Standard deviation and/or SMDD standard deviation
        * CVar
        * Downside deviation below the arithmetic mean return
        * Downside deviation below a target return
        * First lower partial moment below the arithmetic mean return
        * First lower partial moment below a target return

"""
    def mvopt(Portfolio):
        a_rtn_ls = Portfolio.a_rtn_ls
        stdev_ls = Portfolio.stdev_ls
        corr = Portfolio.corr
        cov = corr * np.outer(stdev_ls, stdev_ls)
# cvxopt Quandratic Programming        
# solves the QP, where x is the allocation of the portfolio:
# minimize   x'Px + q'x
# subject to Gx <= h
#            Ax == b
#
# Input:  n       - # of assets
#         avg_ret - nx1 matrix of average returns
#         covs    - nxn matrix of return covariance
#         r_min   - the minimum expected return that you'd
#                   like to achieve
# Output: sol - cvxopt solution object        



        
        








