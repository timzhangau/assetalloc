# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:28:23 2016

@author: tzhang1
"""

import pandas as pd
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
        
        # import NER history
        ner_history = files_path + '/ppp_history.csv'
        ner = pd.read_csv(ner_history, parse_dates=True, index_col=[0])
        ner = ner[self.base_currency]
        
        return cpi, ppi, ppp, ner        
        
    def cal_fair_ner(self, methodology, cpi, ppi, ppp, ner):
        # import fair ner calculation methodology
        methodology = pd.read_csv(methodology, parse_dates=[-1], index_col=[0])
        method = methodology.ix[self.base_currency]['Deflator']
        start_date = methodology.loc[self.base_currency, 'Start_Date']
        
        # index USD price series
        cpi['USD'] = cpi['USD']/cpi['USD'][0]       
        ppi['USD'] = ppi['USD']/ppi['USD'][0] 
        ppp['USD'] = ppp['USD']/ppp['USD'][0] 
        
        # index base currency's country price levels
        cpi[self.base_currency] = cpi[self.base_currency]/cpi.loc[start_date, self.base_currency]
        ppi[self.base_currency] = ppi[self.base_currency]/ppi.loc[start_date, self.base_currency]
        ppp[self.base_currency] = ppp[self.base_currency]/ppp.loc[start_date, self.base_currency]
        
        # calculate price level differentials from U.S.
        cpi_diff = cpi[self.base_currency]/cpi['USD'].values

        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        