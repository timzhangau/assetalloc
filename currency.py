# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:28:23 2016

@author: tzhang1
"""

import pandas as pd



# This is to create a Currency class to store currency pair attributes
# and calculate the Fair Nominal Exchange Rate and Expected Return

class Currency(object):
    def __init__(self, base_currency):
        # initiate currency class, all we need is base currency for start
        self.base_currency = base_currency
        self.cpi = 'cpi series'
        self.ppi = 'ppi series'
        self.ppp = 'ppp series'
        self.ner = 'ner series'
    
    # Functions need to be created
    # 1. import data (this will import deflator series and methodology lookup)
    # 2. calculate fair NER (this is to calculate fair NER for base currency)
    # 3. calculate expected return (calculate expected return as per fair NER results)
    
    def import_data(self, files_path):
        # import cpi history
        cpi_history = files_path + '/cpi_history.csv'
        cpi = pd.read_csv(cpi_history, parse_dates=True, index_col=[0])
        self.cpi = cpi[self.base_currency]
        
        # import ppi history
        ppi_history = files_path + '/ppi_history.csv'
        ppi = pd.read_csv(ppi_history, parse_dates=True, index_col=[0])  
        self.ppi = ppi[self.base_currency]
        
        # import ppp history
        ppp_history = files_path + '/ppp_history.csv'
        ppp = pd.read_csv(ppp_history, parse_dates=True, index_col=[0])
        self.ppp = ppp[self.base_currency]
        
        # import NER history
        ner_history = files_path + '/ppp_history.csv'
        ner = pd.read_csv(ner_history, parse_dates=True, index_col=[0])
        self.ner = ner['USD' + self.base_currency]
        
        
    
        
        
        
        
        
        