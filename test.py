# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from assetalloc.asset import Asset
from assetalloc.portfolio import Portfolio
import matplotlib.pyplot as plt

# upload asset risk, return details and correlation matrix

risk_return = pd.read_csv("returnrisk.csv", index_col=[0])
a_rtn_ls = risk_return['Arithmetic Return']
stdev_ls = risk_return['Standard Deviation']
corr = pd.read_csv("correlation.csv", index_col=[0])
cov = corr * np.outer(stdev_ls, stdev_ls)

asset_list = [Asset(i) for i in a_rtn_ls.index]

for asset in asset_list:
    asset.a_rtn = a_rtn_ls[asset.name]
    asset.stdev = stdev_ls[asset.name]

portfolio1 = Portfolio()
portfolio1.assets = asset_list
portfolio1.corr = corr
portfolio1.cov = cov

returns, risks = portfolio1.efficientfrontier()

# plot efficient frontier
plt.plot(risks, returns)



    
    


