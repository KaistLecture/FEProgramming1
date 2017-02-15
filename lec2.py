# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:46:45 2017

@author: Administrator
"""
'''
import random
r = []
for i in range(100):
    r.append(random.normalvariate(0,1))
'''
#import keypad_problem as kp
from keypad_problem import calcDist
import random

n = 10
simDist = []
for iter in range(10000):
    sn = ""
    for i in range(n):
        rn = random.randint(0,9)
        sn += str(rn)
    res = calcDist(sn)
    simDist.append(res["distance"])















