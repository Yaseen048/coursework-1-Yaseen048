# Write code that prepares your data

import pandas as pd


def clean_data(data_file):
    data_file.drop(data_file.iloc[:,10:], inplace=True, axis=1)
    data_file.drop(data_file.index[16:], inplace=True)


def main():
    df_March_2020 = pd.read_excel('data\weekend-box-office-report-2020-03-13-15.xls', 
    skiprows = 1)

    df_Aug_2020 = pd.read_excel('data\weekend-box-office-report-2020-08-28-30.xls', 
    skiprows = 1)

    df_July_2021 = pd.read_excel('data\weekend-box-office-report-2021-07-23-25.xls', 
    skiprows = 1)
    
    clean_data(df_March_2020)
    clean_data(df_Aug_2020)
    clean_data(df_July_2021)


    print(df_March_2020)


if __name__ == '__main__':
    main()
