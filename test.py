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
%matplotlib inline
import matplotlib.cm as cm

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

name_ls = np.array([portfolio1.assets[i].name for i in range(len(portfolio1.assets))])

returns, risks = portfolio1.efficientfrontier()[0:2]

# plot efficient frontier
portfolio1.plotfrontier()

# plot optimal asset mix with returns as x axis
portfolio1.plotoptimalmix("returns")

# plot optimal asset mix with risk as x axis
portfolio1.plotoptimalmix("risks")


a, b, c = portfolio1.efficientfrontier()
a = np.array(a)
b = np.array(b)
c = np.array(c).T

colors = cm.rainbow(np.linspace(0, 1, len(name_ls)))
plt.stackplot(a, c, colors=colors.tolist())
plt.legend(name_ls, loc='center left', bbox_to_anchor=(1, 0.5))


    
    


