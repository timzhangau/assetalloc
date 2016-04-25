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
        # import data
        currency.import_data('C:/Users/tzhang1/FX/CMA/')
        # calculate fair NER
        currency.cal_fair_ner()
        # convert pandas series to pandas dataframe
        currency_ner_fair = currency.ner_fair.to_frame()
        currency_ner_fair.columns = [currency_name]
        
        # append dataframe to consolidate NER dataframe
        if i == 0:
            fair_ner_history = currency_ner_fair
        else:
            fair_ner_history = fair_ner_history.join(currency_ner_fair)

        fair_ner_history.to_csv('C:/Users/tzhang1/FX/CMA/Fair_NER.csv')        
        
    print 'Calculation Completed'
        
        
        
        