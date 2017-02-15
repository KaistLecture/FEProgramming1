# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:42:24 2017

@author: Administrator
"""
import dateutil.relativedelta as dr
import datetime

def bondprice(today, issuedate, matdate, \
              freq, couponrate, ytm):
    coupon = 100*couponrate/freq
    d = issuedate
    cdate = []
    while d<matdate:
        d = d + dr.relativedelta(months = int(12/freq))
        cdate.append(d)
    return cdate

today = datetime.datetime.today()
issuedate = datetime.datetime(2016,2,15)
matdate = datetime.datetime(2026,2,15)
temp = bondprice(today, issuedate, matdate, \
                 2, 0.04, 0.025)








