import pandas as pd
import numpy as np

# method 1: only use pm2.5 feature
# read training data as n-array
path_file = 'train.csv'
# read file as data-frame.
# Using 'rb' reading method or the best way--gbk, because the file encoding is ANSI
df = pd.read_csv(path_file, encoding='gbk')
data_raw = df.values  # data-frame to n-array

# data pre-process: 1st, '豐原'; 2nd, 'NR' (no rain)
# 'Station' substitute '豐原' in the 2nd column of data_raw
for m in range(data_raw.shape[0]):
    data_raw[m, 1] = 'station'
# 0 substitute 'NR' from 3rd column to last column of data_raw
for m in range(data_raw.shape[0]):
    for n in range(3, data_raw.shape[1]):
        if data_raw[m, n] == 'NR':
            data_raw[m, n] = 0

# training data
x_data = []
y_data = []
# y_data = w[0] + w[1]*x_data + w[2]*x_data

1+1
