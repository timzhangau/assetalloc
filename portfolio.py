# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 11:53:40 2016

@author: tzhang1
"""

import numpy as np
import pandas as pd
from assetalloc.asset import Asset
from cvxopt import matrix
from cvxopt.solvers import qp, options

"""
Methods need to be built for Portfolio object:
    - Calculate portfolio metrics
    - Portfolio Optimization
    - Portfolio Forecasting
"""

class Portfolio(object):
    def __init__(self):
        self.weights = "please load portfolio weights" # weights is a numpy array
        self.assets = "please specify assets list"
        self.corr = np.array([]) # Correlation is a numpy array
        
        # all the below attributes can be obtained from Asset list
        #self.a_rtn_ls = np.array([])
        #self.g_rtn_ls = np.array([])
        #self.stdev_ls = np.array([])
        #self.skew_ls = np.array([])
        #self.kurt_ls = np.array([])
        
        #for asset in self.assets:
        #    self.a_rtn_ls = np.append(self.a_rtn_ls, asset.a_rtn)
        #    self.g_rtn_ls = np.append(self.g_rtn_ls, asset.g_rtn)
        #    self.stdev_ls = np.append(self.stdev_ls, asset.stdev)
        #    self.skew_ls = np.append(self.skew_ls, asset.skew)
        #    self.kurt_ls = np.append(self.kurt_ls, asset.kurt)
        

    def calculate_portfolio_stats(self):
        if np.sum(self.weights) == 1:
            self.a_rtn = np.dot(self.weights, self.a_rtn_ls)  # AR: Arithmetic Return
            self.g_rtn = np.dot(self.weights, self.g_rtn_ls)
            self.cov = self.corr * np.outer(self.stdev_ls, self.stdev_ls)
            self.stdev = np.dot(np.dot(self.weights, self.cov), self.weights)
            self.g_rtn = (1 + self.a_rtn) * exp(-0.5 * (self.stdev**2) * ((1+self.a_rtn)**-2)) -1
        else:
            print 'Check Portfolio Weights, sum not equal to 100%'



#Portfolio Optimization
#Methods:
#   - Mean-Variance Optimization (MVO): traditional Harry Markowitz's MVO method. _
#   It is a single-period optimization, only used to optimize AR and std dev.
#   MVO with Resampling: a combination of Monte Carlo simulation and conventional MVO. _
#   Resample hypothetical return series through Monte Carlo and then calculate hypothetical set _
#   of assumptions. Each set is optimized using MVO to form a set of asset mixes. All asset _
#   mixes are grouped into bins by std dev and then averaged to produce one mix per std dev, _
#   forming the resampled frontier. Still based on MVO, only available for AR and std dev.
#   - Scenario-Based: Use a multivariate Monte Carlo simuation to create hypothetical/simulated_
#   returns data for the parametric models of return distributions. Non-linear optimization _
#   algorithm is then used to find the asset mixes at every level of reward that has the lowest _
#   level of risk.
#
#Return Distribution Assumptions:
#   - Lognormal
#   - Johnson: this account for skew and kurtosis
#   - Bootstrapping: using historical series, account for non-linear co-variance

#Optimization Objective:
#   - Return:
#       * Expected arithmetic mean return: single-period
#       * Expected geometric mean return: multi-period
#   - Risk:
#       * Standard deviation and/or SMDD standard deviation
#       * CVar
#       * Downside deviation below the arithmetic mean return
#       * Downside deviation below a target return
#       * First lower partial moment below the arithmetic mean return
#       * First lower partial moment below a target return


    def mvopt(self, rtn_target, lower_bound=None, upper_bound=None):
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
        
        a_rtn_ls = np.array([self.assets[i].a_rtn for i in range(len(self.assets))])
        stdev_ls = np.array([self.assets[i].stdev for i in range(len(self.assets))])
        name_ls = np.array([self.assets[i].name for i in range(len(self.assets))])
        cov = self.corr.values * np.outer(stdev_ls, stdev_ls)
        n = len(a_rtn_ls)
        
        # Upper bound of the Weights of a equity, If not specified, assumed to be 1.
        if (upper_bound is None):
            upper_bound = np.ones(n)
        upper_bound.shape = (n,1)
    
        # Lower bound of the Weights of a equity, If not specified assumed to be 0 (No shorting case)
        if (lower_bound is None):
            lower_bound = np.zeros(n) 
        lower_bound.shape = (n,1)
                        
        P = matrix(cov)
        q = matrix(0.0, (n,1))
        
        # Constraints Gx <=h, set lower and upper bounds
        I = np.eye(n)
        minusI = -1 * I
        G = matrix(np.vstack((I, minusI)))
        h = matrix(np.vstack((upper_bound, lower_bound)))
        
        # Constraints Ax = b
        # sum(x) = 1
        ones = matrix(1.0, (1,n))
        A = matrix(np.vstack((matrix(a_rtn_ls, (1,n)), ones)))
        b = matrix([float(rtn_target), 1.0])
        
        # Optional Settings for CVXOPT
        options['show_progress'] = False
        sol = qp(P, q, G, h, A, b)
        
        if sol['status'] != 'optimal':
            warnings.warn("Convergence Problem")
        
        op_w = pd.Series(sol['x'], index=name_ls)
        
        return op_w
        
        
    def efficientfrontier(self, simu=100):
        #generate returns list to feed into mvopt
        a_rtn_ls = np.array([self.assets[i].a_rtn for i in range(len(self.assets))])
        stdev_ls = np.array([self.assets[i].stdev for i in range(len(self.assets))])
        rtn_ls = [(max(a_rtn_ls)-min(a_rtn_ls))/100*i+min(a_rtn_ls) for i in range(simu+1)]
        
        returns = []
        risks = []
        
        # call mean-variance optimizer to get optimal weights for each return in the list
        for rtn_target in rtn_ls:
            returns.append(rtn_target)
            op_w = self.mvopt(rtn_target)
            var = np.dot(np.dot(op_w.values, self.cov.values), op_w.values)
            stdev = var ** 0.5
            risks.append(stdev)
            
        return returns, risks
        








