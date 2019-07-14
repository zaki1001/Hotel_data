# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 14:34:17 2019
@author: Zaki
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import datetime
from pandas import DataFrame
url="Hotel_Big_Data.csv"  
df = pd.read_csv(url,index_col=None)
#df=df.drop(['Unnamed: 0'],axis=1)
HighSeason=df    
LowSeason=df
def inptl(HighSeason):
        userweek=raw_input("Week for low season ")
        try:
            userweek=int(userweek)
        except:
            print("Wrong Input Please Enter a Number ")
            #inptl(HighSeason)
            return HighSeason
        HighSeason=seasonh(HighSeason,userweek)
        return HighSeason
def inpth(LowSeason):
        userweek=raw_input("Week for high season ")
        try:
            userweek=int(userweek)
        except:
            print("Wrong Input Please Enter a Number ")
            #inpth(LowSeason)
            return LowSeason
        LowSeason=seasonl(LowSeason,userweek)
        return LowSeason
def seasonh(HighSeason,week):
    HighSeason=HighSeason[HighSeason['WeekNumber']!=week]
    return HighSeason
def seasonl(LowSeason,week):
    LowSeason=LowSeason[LowSeason['WeekNumber']!=week]
    return LowSeason

while True:
    userweek=raw_input("Please Begin Entering The Low Season WeekNumber...Hit Y to Continue and N to start entering High Season WeekNumber ")
    if userweek.lower()=='y' or userweek.lower()=='yes':
        HighSeason=inptl(HighSeason)
    elif userweek.lower()=='n' or userweek.lower()=='no':
        break
    else:
        print("Wrong Input, Please Enter Y for Yes N for No ")
        continue
while True:
    userweek=raw_input("Please Begin Entering The High Season WeekNumber...Hit Y to Continue N to end ")
    if userweek.lower()=='y' or userweek.lower()=='yes':
        LowSeason=inpth(LowSeason)
    elif userweek.lower()=='n' or userweek.lower()=='no':
        break
    else:
        print("Wrong Input, Please Enter Y for Yes N for No ")
        continue 
pd.DataFrame(LowSeason).to_csv("LowSeason.csv",index=None)
pd.DataFrame(HighSeason).to_csv("HighSeason.csv",index=None)
