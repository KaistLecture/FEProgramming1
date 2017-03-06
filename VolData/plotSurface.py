import pandas as pd
import numpy as np
import datetime
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fname = glob.glob('*.csv')
n = len(fname)

fig = plt.figure(figsize=(15,5)) 

for i, f in enumerate(fname):
    data = pd.read_csv(f)
    today = datetime.datetime.strptime(f[-12:-4],'%Y%m%d')
    
    ax = fig.add_subplot(1,n,i+1,projection='3d')
    X = data['Relative Strike'].unique()
    Y = [(datetime.datetime.strptime(d,'%Y/%m/%d')-today).days for d in data['Expiration Date'].unique()]
    Z = np.reshape(data['Volatility'], (len(Y),len(X)))
    X, Y = np.meshgrid(X, Y)
    Y = Y/365
    
    idx = Y[:,0]<=5
    X, Y, Z = X[idx], Y[idx], Z[idx]
    
    ax.plot_wireframe(X,Y,Z)
    ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm)
    ax.view_init(10,300)
    ax.set_title(f.rstrip('.csv'))
    ax.set_xlabel('moneyness')
    ax.set_ylabel('matutity')
    
fig.show()
