import pandas as pd
import glob
import numpy as np
import datetime

def transformdata(filepath,currency):
    df = pd.read_excel(filepath, index_col='Time', parse_dates=True)
    print(df)
    df['Sum'] = df.sum(axis=1)
    names = list(df.columns)
    print(names)

    for i in enumerate(names):
        if i[1] != 'Sum':
            print(i[1])
            df=df.drop(str(i[1]), axis=1)

    print(df)

    df['currency'] = currency

    df.to_excel(f'C:/Users/stank/Stanuska/IES/Bachelor Thesis/DATA/changed_notCRS/{currency}.xlsx', index=True, sheet_name=currency)

#transformdata('C:/Users/stank/Stanuska/IES/Bachelor Thesis/DATA/bitcoinity_dataXAU.xlsx', 'XAU')


path =r'C:/Users/stank/Stanuska/IES/Bachelor Thesis/DATA/changed_notCRS'
filenames = glob.glob(path + "/*.xlsx")

dfs = []
for filename in filenames:
     dfs.append(pd.read_excel(filename, index='Time', parse_dates=True))
     print(pd.read_excel(filename, index='Time', parse_dates=True))





#Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=False, axis='rows')
print(big_frame)
big_frame.to_excel(f'C:/Users/stank/Stanuska/IES/Bachelor Thesis/DATA/big.xlsx', index=True, sheet_name='all')
