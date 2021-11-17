# Write code that prepares your data

import pandas as pd


def clean_data(data_file):
    """cleans data by removing unwanted data and adding date

    args:
        data_file (dataframe): dataframe containg data about movie sales at cinemas
    """
    data_file.drop(data_file.iloc[:,10:], inplace=True, axis=1)#removed empty columns
    data_file.drop(data_file.index[15:], inplace=True)#see only top 15 movies
    data_file.drop(['Rank', '% change on last week', 'Number of cinemas',
    'Site average', 'Total Gross to date'], inplace=True, axis = 1)#remove unwanted data
    data_file['Date'] = data_file.name#added date

def merge(data_file1, data_file2, data_file3):
    """merges 3 dataframes into one data frame
    
    args:
        data_file1 (dataframe): dataframe for movie sales in a specific month
        data_file2 (dataframe): dataframe for movie sales in a specific month
        data_file3 (dataframe): dataframe for movie sales in a specific month
        
    return:
        prepared_data (dataframe): dataframe containing all data of 3 months"""
    merge_data = [data_file1, data_file2, data_file3]
    prepared_data = pd.concat(merge_data)
    return prepared_data

def main():
    df_March_2020 = pd.read_excel('data\weekend-box-office-report-2020-03-13-15.xls', 
    skiprows = 1)
    df_March_2020.name = 'March 2020' #code by user aznbanana9 on stackoverflow,
    #url:https://stackoverflow.com/questions/31727333/get-the-name-of-a-pandas-dataframe
    #date of retrieval: 17/11/2021

    df_Aug_2020 = pd.read_excel('data\weekend-box-office-report-2020-08-28-30.xls', 
    skiprows = 1)
    df_Aug_2020.name = 'Aug 2020'#code by user aznbanana9 on stackoverflow,
    #url:https://stackoverflow.com/questions/31727333/get-the-name-of-a-pandas-dataframe
    #date of retrieval: 17/11/2021

    df_July_2021 = pd.read_excel('data\weekend-box-office-report-2021-07-23-25.xls', 
    skiprows = 1)
    df_July_2021.name = 'July 2021'#code by user aznbanana9 on stackoverflow,
    #url:https://stackoverflow.com/questions/31727333/get-the-name-of-a-pandas-dataframe
    # date of retrieval: 17/11/2021

    clean_data(df_March_2020)
    clean_data(df_Aug_2020)
    clean_data(df_July_2021)

    prepared_data = merge(df_March_2020, df_Aug_2020, df_July_2021)

    prepared_data.to_csv("Prepared_dataset.csv", index=False)



if __name__ == '__main__':
    main()
