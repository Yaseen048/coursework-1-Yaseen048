# Write code that prepares your data

import pandas as pd

df_March_2020 = pd.read_excel('data\weekend-box-office-report-2020-03-13-15.xls', skiprows = 1)

print(df_March_2020)