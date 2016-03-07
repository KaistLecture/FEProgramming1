
import datetime
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

f = open("EQ_Volatility_2016-01-14_0300_LON.csv","r")

mat, stk, vol = [], [], []
for x in f:
    data = x.split(",")
    data[-1] = data[-1].strip("\n")
    if data[1]=="KOSPI 200":
        today = datetime.datetime.strptime(data[0],"%Y-%m-%d")
        matDate = datetime.datetime.strptime(data[7],"%Y-%m-%d")
        stk.append(int(data[8]))
        mat.append((matDate-today).days/365.0)
        vol.append(float(data[-1]))

mat = np.array(mat)
stk = np.array(stk)
vol = np.array(vol)
mat.shape, stk.shape, vol.shape = (14, 11), (14, 11), (14, 11)

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(stk, mat, vol, linewidth=1, rstride=1, cstride=1, cmap=cm.coolwarm)

f.close()