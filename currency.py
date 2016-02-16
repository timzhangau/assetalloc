# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:28:23 2016

@author: tzhang1
"""

# This is to create a Currency class to store currency pair attributes
# and calculate the Fair Nominal Exchange Rate and Expected Return

class Currency(object):
    def __init__(self, base_currency):
        # initiate currency class, all we need is base currency for start
        self.base_currency = base_currency
    
    # Functions need to be created
    # 1. import data (this will import deflator series and methodology lookup)
    # 2. calculate fair NER (this is to calculate fair NER for base currency)
    # 3. calculate expected return (calculate expected return as per fair NER results)
    
    def import_data(self, files_path):
        cpi_history = files_path + '/cpi_history.csv'
        cpi = pd.read_csv(cpi_history, parse_dates=True, index_col=[0])
    
    