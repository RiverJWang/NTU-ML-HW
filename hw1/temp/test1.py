import pandas as pd
import numpy as np
from pandas import DataFrame
import math

path_file = r"C:\Users\40664\Desktop\NTU-EXP-CODE-PYTHON\NTU-ML-HW\hw1\train.csv"

train=pd.read_csv(path_file, encoding='gbk');
# pm=train[train[""]]
pm=train[train["測項"]=="PM2.5"]
pm.drop(['日期','測站','測項'],axis=1,inplace=True)  # axis=0 is column, axis=1 is raw and using ''日期'','9'
x=[]# 此时x,y为list
y=[]
for i in range(15):#冒号
    temx=pm.iloc[:,i:i+9]
    temx.columns=np.array(range(9))
    temy=pm.iloc[:,i+9]
    temy.columns=np.array(range(1))
    x.append(temx)
    y.append(temy)

x=pd.concat(x)#3600x9,3600=240x15,此时x为dataframe
y=pd.concat(y)#3600x1 ,y为serise
x=np.array(x,float)
y=np.array(y,float)
np.save(r"C:\Users\40664\Desktop\NTU-EXP-CODE-PYTHON\NTU-ML-HW\hw1\temp\x.npy",x)
np.save(r"C:\Users\40664\Desktop\NTU-EXP-CODE-PYTHON\NTU-ML-HW\hw1\temp\y.npy",y)

1+1