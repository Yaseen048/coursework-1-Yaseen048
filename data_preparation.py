# Write code that prepares your data

import pandas as pd

df_March_2020 = pd.read_excel('data\weekend-box-office-report-2020-03-13-15.xls', 
skiprows = 1)

df_Aug_2020 = pd.read_excel('data\weekend-box-office-report-2020-08-28-30.xls', 
skiprows = 1)

df_July_2021 = pd.read_excel('data\weekend-box-office-report-2021-07-23-25.xls', 
skiprows = 1)

def clean_data(data_file):
    data_file.drop(data_file.iloc[:,10:], inplace=True, axis=1)
    data_file.drop(data_file.index[16:], inplace=True)


def main():
    clean_data(df_March_2020)
    print(df_March_2020)

#df_March_2020.drop(df_March_2020.iloc[:,10:], inplace=True, axis=1)
#df_March_2020.drop(df_March_2020.index[16:], inplace=True)
if __name__ == '__main__':
    main()
#print(df_March_2020)