import numpy as np
import pandas as pd

model = np.load("model.npy")
w = model
test = pd.read_csv(r"..\test.csv", header=None)
t = test[test[1] == "PM2.5"]
t.drop([0, 1], axis=1, inplace=True)
t = np.array(t, float)
t = np.concatenate((np.ones((t.shape[0], 1)), t), axis=1)

res = np.dot(t, w)
1+1