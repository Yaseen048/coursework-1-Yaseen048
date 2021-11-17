# Write code that explores your data set

import pandas as pd

def total(data):
    """returns the total weekend sales for March 2020, August 2020 and July 2021
    
    args:
    data (dataframe) = dataframe containing cleaned data of movies in cinemas of months
                            March 2020, August 2020 and July 2021
    """
    March_2020 = data[data["Date"] == "March 2020"]#using data from march
    March_2020_total = March_2020["Weekend Gross"].sum()
    #total of one weekend gross in March

    Aug_2020 = data[data["Date"] == "Aug 2020"]#using data from August
    Aug_2020_total = Aug_2020["Weekend Gross"].sum()
    #total of one weekend gross in August

    July_2021 = data[data["Date"] == "July 2021"]#using data from July
    July_2021_total = July_2021["Weekend Gross"].sum()
    #total of one weekend gross in July

    print("The total weekend gross for all movies for a week in a month:\n\
March 2020 = £{0}\nAugust 2020 = £{1}\nJuly 2021 = £{2}"\
.format(March_2020_total, Aug_2020_total, July_2021_total))

    return(March_2020_total, Aug_2020_total, July_2021_total)




def main():
    df = pd.read_csv("Prepared_dataset.csv")
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.expand_frame_repr', False)

    total(df)


if __name__ == '__main__':
    main()
