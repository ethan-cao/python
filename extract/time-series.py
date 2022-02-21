import csv
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from datetime import datetime


def mdy_to_ymd(d):
    return datetime.strptime(d, '%B %d, %Y').strftime('%Y-%m-%d')

cd = pd.read_csv('time_cn.csv', encoding='utf-8')


# TODO: get a list of new dates
# input: df['Date']: Series
# output: new_dates: list[string]
new_dates = []
for date in df['Date']:
    # TODO: transform format
    # input:  date: String
    # output: new_date: String
    new_date = mdy_to_ymd(date)

    # collect new format
    new_dates.append(new_date)

# TODO: add new_dates to df as a new column 
# input: new_dates: list[string]
# output: df['New_Date'] has the new column
 

df['New_Date'] = new_dates



# TODO
# input:  var1: Type1
# output: var2: Type2

# TODO2
# input:  var2: Type2
# output: var3: Type3