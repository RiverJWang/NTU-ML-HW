import pandas as pd
import numpy as np
from pandas import DataFrame
import math

x=np.load(r"C:\Users\40664\Desktop\NTU-EXP-CODE-PYTHON\NTU-ML-HW\hw1\temp\x.npy")
y=np.load(r"C:\Users\40664\Desktop\NTU-EXP-CODE-PYTHON\NTU-ML-HW\hw1\temp\y.npy")
#adding baias
x = np.concatenate((np.ones((x.shape[0],1)),x), axis=1)  # add a 3600col's one vector
#init
w = np.zeros(len(x[0]))
l_rate = 10
repeat = 10000
s_grad=np.zeros(len(x[0]))
x_t=x.transpose()
# train
for i in range(repeat):
    tem=np.dot(x,w)
    loss=tem-y
    grad=np.dot(x_t,loss)
    s_grad+=grad**2
    ada=np.sqrt(s_grad)
    w=w-l_rate*grad/ada
np.save("model.npy",w)

1+1