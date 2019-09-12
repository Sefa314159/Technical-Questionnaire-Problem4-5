import numpy as np
import pandas as pd

# loading "i_users.csv" as DataFrame
df1 = pd.read_csv("i_users.csv")

# loading "i_user_login_logs.csv" as DataFrame
df2 = pd.read_csv("i_user_login_logs.csv")

# to find who logged in most
a = df2["userld"].max()

# to find who logged in most in "i_user_login_logs.csv"
# using fancy index
b = df2[df2["userld"] == df2["userld"].max()]

# to find who logged in most in "i_users.csv"
problem5 = df1[df2["userld"] == df2["userld"].max()]

# solution to our problem:
problem5.iloc[:, 1:3]
