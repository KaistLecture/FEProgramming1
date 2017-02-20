# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:52:12 2017

@author: K.Hwang
"""

import scipy.optimize as sop
from bondpricing import bondprice
import datetime

today = datetime.datetime.today()
issuedate = datetime.datetime(2016,2,15)
matdate = datetime.datetime(2026,2,15)
freq = 4
couponRate = 0.04
ytm = 0.03
mktPrice = 98.5

func = lambda y: bondprice(today, issuedate, matdate, freq, couponRate, y) - mktPrice

x = sop.fsolve(func, 0.03)
price = bondprice(today, issuedate, matdate, freq, couponRate, x)
print("YTM = {0:0.2%}".format(x[0]))
print("Price = {0:0.3f}".format(price))