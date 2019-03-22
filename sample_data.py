import numpy as np
import pandas as pd
from pandas import DataFrame 

def get_data_norm():
    data = np.random.normal(1, 3, 900)
    return DataFrame(data = data)

def get_data_csv(filepath = './santaba-demo4.csv', data_column = 'prod08.ld5'):
    data = pd.read_csv(filepath)
    data = data.rename(columns = {'Time': 'ds', data_column: 'y'})
    data.set_index('ds')
    __fix_none_data(data)
    return data

def iter_data(data, block_size = 60):
    for i in range(len(data) - block_size):
        eval_data = data[i : i + block_size]
        yield eval_data
        
def __fix_none_data(data_frame):
    for index, row in data_frame.iterrows():
        if isinstance(row['y'], str) and row['y'].strip() == 'No Data':
            row.loc['y'] = None
            data_frame.loc[index] = row
    