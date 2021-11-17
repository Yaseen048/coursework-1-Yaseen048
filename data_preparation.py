# Write code that prepares your data

import pandas as pd


def clean_data(data_file):
    data_file.drop(data_file.iloc[:,10:], inplace=True, axis=1)#removed empty columns
    data_file.drop(data_file.index[15:], inplace=True)#see only top 15 movies
    data_file.drop(['Rank', '% change on last week', 'Number of cinemas',
    'Site average', 'Total Gross to date'], inplace=True, axis = 1)#remove unwanted data
    data_file['Date'] = data_file.name#added date

def main():
    df_March_2020 = pd.read_excel('data\weekend-box-office-report-2020-03-13-15.xls', 
    skiprows = 1)
    df_March_2020.name = 'March 2020' #code by user aznbanana9 on stackoverflow,
    #url: , date of retrieval: 17/11/2021

    df_Aug_2020 = pd.read_excel('data\weekend-box-office-report-2020-08-28-30.xls', 
    skiprows = 1)
    df_Aug_2020.name = 'Aug 2020'#code by user aznbanana9 on stackoverflow,
    #url: , date of retrieval: 17/11/2021

    df_July_2021 = pd.read_excel('data\weekend-box-office-report-2021-07-23-25.xls', 
    skiprows = 1)
    df_July_2021.name = 'July 2021'#code by user aznbanana9 on stackoverflow,
    #url: , date of retrieval: 17/11/2021

    clean_data(df_March_2020)
    clean_data(df_Aug_2020)
    clean_data(df_July_2021)


    print(df_March_2020)


if __name__ == '__main__':
    main()
