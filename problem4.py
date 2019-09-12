import numpy as np
import pandas as pd

# loading "i_users.csv" as DataFrame
df1 = pd.read_csv("i_users.csv")

# loading "i_user_login_logs.csv" as DataFrame
df2 = pd.read_csv("i_user_login_logs.csv")

# users who logged in more than three times in "i_user_login_logs.csv"
a = df2[df2["userld"] > 3]

# users who logged in more than three times in "i_users.csv"
# using fancy index
problem4 = df1[df2["userld"] > 3]

# solution to our problem:
problem4["username"]
