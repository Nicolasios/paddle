TOTAL_SIZE = 100
K = 2
B = 2
BIAS = 2
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(start=1,stop=2*TOTAL_SIZE,num=TOTAL_SIZE)

bias = np.random.randint(low=-BIAS,high=BIAS,size=TOTAL_SIZE,dtype=int)

y = K*x+B+bias

df = pd.DataFrame({'x':x,'y':y})
df.to_csv("./Z_TY/data.csv",index=False)

# plt.show()

