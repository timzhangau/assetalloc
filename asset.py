# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 15:40:32 2016

@author: tzhang1
"""

# This is to create an Asset class to store risk and 
# return attributes

import numpy as np
import pandas as pd




class Asset(object):
    def __init__(self, name):
        self.name = name #asset name
        self.a_rtn = "please upload asset AR"
        self.g_rtn = "please upload asset GR"      
        # Asset return can be modelled using different methods:
        # Building Block, CAPM, Black-Litterman and Historical Data.
        # This attribute is only the final output of different methods.
        self.stdev = "please upload asset standard deviation"
        # Risk measures can be modelled using factor-model.
        # This attribute is only the final output of risk model.
        self.skew = "please upload asset skewness"
        self.kurt = "please upload asset kurtosis"
        self.history = "please upload asset history"
        self.currency = "please upload asset currency"
    
    

# Methods need to be built for Asset object:
#    - Return Assumption Methods: Building Block, CAPM, Black-Litterman and Historical
#    - Risk Assumption Methods: Risk Factor Model for stdev, skew and kurt. Correlation _
#    matrix is a method under portfolio objects
#    - Conversion between arithmetic mean and geometric mean

    def artogr(self):
        self.g_rtn = (1 + self.a_rtn) * exp(-0.5 * (self.stdev**2) * ((1+self.a_rtn)**-2)) -1

            
        
        
        
        
        
        
        