# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 15:40:32 2016

@author: tzhang1
"""

# This is to create an Asset class to store risk and 
# return attributes

import numpy as np
import pandas as pd


# create asset class object, this is to feed into portfolio class for portfolio construction

class Asset(object):
    def __init__(self):
        self.name = "please specify asset class name" #asset name
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





class Equity(Asset):
    def __init__(self):
        Asset.__init__(self)
        self.cls = "Equity"
        self.div_yld = "please upload div yield data"
        self.div_po = "please upload div payout data"
        self.div_growth = "please upload div growth data"
        self.pe = "please upload pe data"
        self.cape10 = "please upload 10Y cape data"
        self.cape5 = "please upload 5Y cape data"
        self.eps_growth = "please upload eps growth data"
        self.price = "please upload price data"
        self.tot_ret = "please upload total return price data"
        self.pb = "please upload price to book data"
        self.roe = "please upload roe data"
        self.bps_growth = "please upload bps growth data"
        self.pcf = "please upload price to cashflow data"
        self.cfps_growth = "please upload cfps growth data"
        self.ps = "please upload price to sales data"
        self.margin = "please upload margin data"
        self.sps_growth = "please upload sps growth data"
        self.tot_yld = "please upload total yield data"
        self.caty10 = "please upload 10Y caty data"
        self.caty5 = "please upload 5Y caty data"
        self.tot_po = "please upload total yield payout data"
        self.tot_growth = "please upload total payout growth data"
        self.net_iss = "please upload net issuance data"
        self.mkt_cap = "please upload total mkt cap data"
        self.reprch_yld = "please upload repurchase yield data"
        self.iss_yld = "please upload issuance yield data"
        self.sec_w = "please upload sector weight"
        self.region = "please specify region"
        self.inflation = "please upload inflation data"
        
        
        
        
    def importdata(self):
        mapping = pd.read_csv("mapping.csv", index_col=[0])
        data = pd.read_csv("ausequity.csv", index_col=[0], parse_dates=True, dayfirst=True)
        for i in range(len(mapping.index)):
            attribute = mapping.index[i]
            setattr(self, attribute, data[mapping.iloc[i,0]])

        self.earnings_norm = self.price/self.pe
        
        # assume total yield equals to div yield at this stage, need to update this once data available
        self.tot_yld = self.div_yld
        

    def assumptions(self):
        #this is to calculate assumptions used in the model, fair growth rate, payout ratio and etc
        #currently the fair assumptions are hard coded, need to complete this function once data available
        self.trend_fair = 0.0163
        self.pe_fair = 14.74
        self.margin_fair = 0.0696
        self.roe_fair = 0.109
        self.tpo_fair = 0.7242
    
    
    def fairreturns(self):
        self.income













        
        
        
        
        
        