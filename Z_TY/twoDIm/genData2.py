TOTAL_SIZE = 1000
K1 = 2
k2 = 3
B = 2
BIAS = 2
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.random.randint(low=1,high=TOTAL_SIZE,size=TOTAL_SIZE)
y = np.random.randint(low=TOTAL_SIZE,high=3*TOTAL_SIZE,size=TOTAL_SIZE)

bias = np.random.randint(low=-BIAS,high=BIAS,size=TOTAL_SIZE,dtype=int)

z = K1 * x + k2 * y + B + bias

df = pd.DataFrame({'x':x,'y':y,'z':z})
# df.to_csv("./Z_TY/data/data2.csv",index=False)



import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x,y,z,color='red')
ax.scatter(x,y,2*x+3*y+2,color='blue')

# 2.3显示
plt.show()

# plt.show()

