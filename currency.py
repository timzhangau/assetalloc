# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:28:23 2016

@author: tzhang1
"""

import pandas as pd
import numpy as np
from datetime import datetime


# This is to create a Currency class to store currency pair attributes
# and calculate the Fair Nominal Exchange Rate and Expected Return

class Currency(object):
    def __init__(self, base_currency):
        # initiate currency class, all we need is base currency for start
        self.base_currency = base_currency
        self.cpi = 'please load cpi series'
        self.ppi = 'please load ppi series'
        self.ppp = 'please load ppp series'
        self.ner = 'please load ner series'
    
    # Functions need to be created
    # 1. import data (this will import deflator series and methodology lookup)
    # 2. calculate fair NER (this is to calculate fair NER for base currency)
    # 3. calculate expected return (calculate expected return as per fair NER results)
    
    def import_data(self, files_path):
        # import cpi history
        cpi_history = files_path + '/cpi_history.csv'
        cpi = pd.read_csv(cpi_history, parse_dates=True, index_col=[0])
        cpi = cpi[['USD', self.base_currency]]
        
        # import ppi history
        ppi_history = files_path + '/ppi_history.csv'
        ppi = pd.read_csv(ppi_history, parse_dates=True, index_col=[0])  
        ppi = ppi[['USD', self.base_currency]]
        
        # import ppp history
        ppp_history = files_path + '/ppp_history.csv'
        ppp = pd.read_csv(ppp_history, parse_dates=True, index_col=[0])
        ppp = ppp[['USD', self.base_currency]]
        
        # import NER history. NER is expressed in "USDXXX" format
        ner_history = files_path + '/ppp_history.csv'
        ner = pd.read_csv(ner_history, parse_dates=True, index_col=[0])
        ner = ner[self.base_currency]
        
        return cpi, ppi, ppp, ner        
        
    def cal_fair_ner(self, methodology, cpi, ppi, ppp, ner):
        # import fair ner calculation methodology
        methodology = pd.read_csv(methodology, parse_dates=[-1], index_col=[0])
        method = methodology.ix[self.base_currency]['Deflator']
        start_date = methodology.loc[self.base_currency, 'Start_Date']

        ner = 1/ner[self.base_currency]        
        
        # index USD price series
        cpi['USD'] = cpi['USD']/cpi['USD'][0]       
        ppi['USD'] = ppi['USD']/ppi['USD'][0] 
        ppp['USD'] = ppp['USD']/ppp['USD'][0] 
        
        # index base currency's country price levels
        cpi[self.base_currency] = cpi[self.base_currency]/cpi.loc[start_date, self.base_currency]
        ppi[self.base_currency] = ppi[self.base_currency]/ppi.loc[start_date, self.base_currency]
        ppp[self.base_currency] = ppp[self.base_currency]/ppp.loc[start_date, self.base_currency]
        
        # calculate price level differentials from U.S.
        cpi_diff = cpi[self.base_currency]/cpi['USD']
        cpi_diff.columns = self.base_currency
        
        ppi_diff = ppi[self.base_currency]/ppi['USD']
        ppi_diff.columns = self.base_currency
        
        ppp_diff = ppp[self.base_currency]/ppp['USD']
        ppp_diff.columns = self.base_currency
        
        # calculate real exchange rate using RER=NERxP/P*, where P* is foreign price level (U.S. in this case)
        # RER is expressed here in "XXXUSD" format        
        rer_cpi = ner * cpi_diff
        rer_ppi = ner * ppi_diff
        rer_ppp = ner * ppp_diff
        rer_avg2 = (rer_cpi + rer_ppi) / 2
        
        # calculate historical averages using pandas expanding_mean function       
        rer_cpi_mean = np.exp(pd.expanding_mean(np.log(rer_cpi)))
        rer_ppi_mean = np.exp(pd.expanding_mean(np.log(rer_ppi)))
        rer_ppp_mean = np.exp(pd.expanding_mean(np.log(rer_ppp)))
        rer_avg2_mean = np.exp(pd.expanding_mean(np.log(rer_avg2)))
        
        #calculate Fair RER assuming "Current RER/Current NER = Fair RER/Fair NER"
        ner_cpi_fair = rer_cpi_mean/(rer_cpi/ner)
        ner_ppi_fair = rer_ppi_mean/(rer_ppi/ner)
        ner_ppp_fair = rer_ppp_mean/(rer_ppp/ner)
        ner_avg2_fair = rer_avg2_mean/(rer_avg2/ner)
        
        # calculate current valuation deviation from fair NER
        val_diff_cpi = ner/ner_cpi_fair - 1
        val_diff_ppi = ner/ner_ppi_fair - 1
        val_diff_ppp = ner/ner_ppp_fair - 1
        val_diff_avg2 = ner/ner_avg2_fair - 1
        
        # calculate fair NER based on calculation methodology
        if method = 'PPP/CPI':
            ner_fair = 1
        elif method = 'PPP/CPI/PPI':
            ner_fair = 2
        elif method = 'PPP':
            ner_fair = 3
        elif method = 'CPI/PPI':
            ner_fair = 4
        elif method = 'PPI':
            ner_fair = 5
            
        return ner_fair[-1]
        
                
        
        
        

        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        