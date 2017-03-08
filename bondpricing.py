# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:42:24 2017

@author: Administrator
"""
import dateutil.relativedelta as dr
import datetime
import math 

def bondprice(today, issuedate, matdate, freq, couponrate, ytm):
    coupon = 100*couponrate/freq
    d = issuedate
    cdate = []
    while d<matdate:
        d = d + dr.relativedelta(months = int(12/freq))
        cdate.append(d)
    t = [(i-today).days/365 for i in cdate]
    s = 0
    for i in t:
        if i>0:
            s += coupon * math.exp(-ytm*i)
    s += 100 * math.exp(-ytm*t[-1])
    return s

if __name__=="__main__":
    today = datetime.datetime.today()
    issuedate = datetime.datetime(2016,2,15)
    matdate = datetime.datetime(2026,2,15)
    ytm = 0.03
    freq = 4
    couponrate = 0.04
    temp = bondprice(today, issuedate, matdate, freq, couponrate, ytm)
    print(temp)

    import matplotlib.pyplot as plt
    import numpy as np
    yields = np.linspace(0.01, 0.1, 10)
    prices = [bondprice(today, issuedate, matdate, freq, couponrate, y) for y in yields]
    plt.plot(yields, prices, '-o')
    plt.show()





