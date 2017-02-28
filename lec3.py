# -*- coding: utf-8 -*-
import datetime
import bondpricing
from bondpricing import bondprice

today = datetime.datetime.today()
issuedate = datetime.datetime(2016,2,15)
matdate = datetime.datetime(2026,2,15)
ytm = 0.03
freq = 4
couponrate = 0.04
temp = bondprice(today, issuedate, matdate, freq, couponrate, ytm)
print(temp)