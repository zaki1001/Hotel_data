# -*- coding: utf-8 -*-
"""
Created on Sun Apr 07 17:10:34 2019

@author: Zaki
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import datetime
from pandas import DataFrame
import os 
cw=os.getcwd()
print cw
dirs=os.listdir( cw )
print dirs
for file in dirs:
    if file.endswith("csv"):
        if "Thomas" in file:
            url1=file
df = pd.read_csv(url1,index_col=None)
url="Hotel_Big_Data.csv" 
Hotel_Big_Data=pd.read_csv(url,index_col=None)
try:
    for i in range(0,len(df['Name'])):
        arrival1=df.loc[[i],['Check-in']]
        arrival=arrival1.iloc[0]
        arrival=max(arrival)
        checkin=datetime.datetime.strptime(arrival,'%m/%d/%Y')
        checkin=checkin.date()
        checkin1=checkin.strftime("%#m/%#d/%Y")
        night=df.loc[[i],['Nights']]
        night=night.iloc[0]
        night=max(night)
        date_made=df.loc[[i],['Date Made']]
        date_made=date_made.iloc[0]
        date_made=max(date_made)
        date_made=datetime.datetime.strptime(date_made,'%m/%d/%Y')
        date_made=date_made.date()
    
        def upd(checkin1):
          #try:
            B=Hotel_Big_Data.loc[Hotel_Big_Data['Date of arrival']==checkin1]
            E=B.iloc[0].astype(str)
            F=E['Date of arrival']
            F1=datetime.datetime.strptime(F,'%m/%d/%Y')
            F=F1.date()
            B1=Hotel_Big_Data.loc[Hotel_Big_Data['Date of arrival']==checkin1].index.values.astype(int)
            Minus=F-date_made
            Minus=Minus.days
            if Minus==0:
                Hotel_Big_Data.at[B1,'Same day']=Hotel_Big_Data.loc[B1,'Same day']+1
            elif Minus==1:
                Hotel_Big_Data.at[B1,'One day out']=Hotel_Big_Data.loc[B1,'One day out']+1
            elif Minus==2:
                Hotel_Big_Data.at[B1,'Two days out']=Hotel_Big_Data.loc[B1,'Two days out']+1
            elif Minus==3:
                Hotel_Big_Data.at[B1,'Three days out']=Hotel_Big_Data.loc[B1,'Three days out']+1
            elif Minus==4:
                Hotel_Big_Data.at[B1,'Four days out']=Hotel_Big_Data.loc[B1,'Four days out']+1                  
            elif Minus==5:
                Hotel_Big_Data.at[B1,'Five days out']=Hotel_Big_Data.loc[B1,'Five days out']+1
            elif Minus==6:
                Hotel_Big_Data.at[B1,'Six days out']=Hotel_Big_Data.loc[B1,'Six days out']+1
            elif Minus==7:
                Hotel_Big_Data.at[B1,'Seven days out']=Hotel_Big_Data.loc[B1,'Seven days out']+1
            elif 7<Minus<=14:
                Hotel_Big_Data.at[B1,'One week out']=Hotel_Big_Data.loc[B1,'One week out']+1
            elif 14<Minus<=21:
                Hotel_Big_Data.at[B1,'Two weeks out']=Hotel_Big_Data.loc[B1,'Two weeks out']+1
            elif 21<Minus<=365:
                Hotel_Big_Data.at[B1,'remaining period']=Hotel_Big_Data.loc[B1,'remaining period']+1
            else:
                k=0;
            
          #except:
              #''''''
        
        if night>1:
            for j in range(0,int(night)): 
                    newcheckin=checkin+datetime.timedelta(days=j)
                    newcheckin1=newcheckin.strftime("%#m/%#d/%Y")
                    upd(newcheckin1)
        elif night==1 or night==0:
            upd(checkin1)
           # #for j in range(0,int(night)): 
                
                #newcheckin=checkin+datetime.timedelta(days=0)
                #newcheckin1=newcheckin.strftime("%#m/%#d/%Y")
                #upd(newcheckin1)
except:
    ''''''
#Hotel_Big_Data=Hotel_Big_Data.at[B1,'Two weeks out']=Hotel_Big_Data.loc[B1,'WeekNumber']+1
    #if arrival==
#LowSeason=Hotel_Big_Data.groupby(['WeekDay']).min()
#HighSeason=Hotel_Big_Data.groupby(['WeekDay']).max()
file_name='Hotel_Big_Data.csv'
Hotel_Big_Data.to_csv(file_name, encoding='utf-8', index=None) 
