# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:41:43 2019

@author: Ram
"""

n=int(input())
str=input()
sealvl=0
valley=0
for x in range(n):
    if str[x]=="U":
        sealvl+=1
    if str[x]=="D":
        sealvl-=1
    if sealvl==0 and str[x]=="U":
        valley+=1
print(valley)