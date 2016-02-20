# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:46:24 2016

@author: tzhang1
"""

from assetalloc.currency import Currency
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # import currency list
    currency_list = pd.read_csv('C:/Users/tzhang1/FX/CMA/Currency_List.csv')
    
    # loop through currency list to calculate Fair NER
    for i in range(len(currency_list)):
        currency_name = currency_list.iloc[i, 0]
        currency = Currency(currency_name)
        currency.import_data('C:/Users/tzhang1/FX/CMA/')
        currency.cal_fair_ner()
        
        
        
        