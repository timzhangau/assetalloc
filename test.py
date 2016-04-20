# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

risk_return = pd.read_csv("returnrisk.csv", index_col=[0])
a_rtn_ls = risk_return['Arithmetic Return']
stdev_ls = risk_return['Standard Deviation']
corr = pd.read_csv("correlation.csv", index_col=[0])
cov = corr * np.outer(stdev_ls, stdev_ls)

asset_ls = a_rtn_ls.index
