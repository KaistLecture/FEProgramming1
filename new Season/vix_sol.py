
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("vix_data.xlsx")
data.index = data.pop("DATE")
data.dropna(inplace=True)
data["SP500"] = np.log(data["SP500"])
r = data.diff()

fig, ax = plt.subplots(1,1,figsize=(6,4))
ax.scatter(x=r["SP500"], y=r["VIXCLS"],marker='+')
model = pd.ols(x=r["SP500"], y=r["VIXCLS"])
alpha = model.beta.intercept
beta = model.beta.x
x = np.array([-0.15,0.15])
y = alpha + beta*x
ax.plot(x,y,'r-')
ax.text(0,20,r"$\Delta VIX_t ={0:0.3f}+{1:0.3f}\Delta logS_t$".format(alpha, beta), fontsize=15)
ax.set_xlabel(r"$\Delta log S_t$")
ax.set_ylabel(r"$\Delta VIX_t$")
fig.show()


rv = pd.rolling_std(r["SP500"], window=20) * np.sqrt(252)
model1 = pd.ols(x=data["VIXCLS"]/100.0, y=rv)
alpha1 = model1.beta.intercept
beta1 = model1.beta.x
x1 = np.array([0,0.9])
y1 = alpha1 + beta1*x1

fig1, ax1 = plt.subplots(1,2,figsize=(10,4))
ax1[0].scatter(x=data["VIXCLS"]/100.0,y=rv,marker=".")
ax1[0].plot(x1,y1,'r-')
ax1[0].set_xlabel("VIX")
ax1[0].set_ylabel("Historical Vol")
ax1[0].text(-0.15,1.0,r"$Y ={0:0.3f}+{1:0.3f}X+\epsilon$".format(alpha1, beta1), fontsize=15)

ax1[1].plot(data["VIXCLS"]/100.0)
ax1[1].plot(rv)

