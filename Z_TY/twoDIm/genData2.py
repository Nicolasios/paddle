TOTAL_SIZE = 100
K1 = 2
k2 = 3
B = 2
BIAS = 2
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(start=1,stop=2*TOTAL_SIZE,num=TOTAL_SIZE)
y = np.linspace(start=TOTAL_SIZE,stop=3*TOTAL_SIZE,num=TOTAL_SIZE)

bias = np.random.randint(low=-BIAS,high=BIAS,size=TOTAL_SIZE,dtype=int)

z = K1 * x + k2 * y + B + bias

df = pd.DataFrame({'x':x,'y':y,'z':z})
df.to_csv("./Z_TY/data/data2.csv",index=False)

# plt.show()

