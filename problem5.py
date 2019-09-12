# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:33:01 2019

@author: Sefa3
"""

import numpy as np
import pandas as pd

# loading "i_users.csv" as DataFrame
df1 = pd.read_csv("i_users.csv")

# loading "i_user_login_logs.csv" as DataFrame
df2 = pd.read_csv("i_user_login_logs.csv")

logs = []
for i in range(2, len(df1["userld"]) + 1):
    m, n = df2[df2["userld"] == i].iloc[:, 0:1].shape
    logs.append(m)

j = max(logs)
x = logs.index(j) + 1

df1.iloc[x:x+1, 1:3]
