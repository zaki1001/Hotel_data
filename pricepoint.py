# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:28:28 2019
@author: Zaki
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import datetime
from pandas import DataFrame
import re
import os
import csv
#P(0) VALUEA<B-25<C-35<E-40<F-35<G-70
#3to13

url="pricepoint.csv" 
tt=pd.read_csv(url,index_col=None,date_parser=[1])
url1="Hotel_Big_Data.csv" 
df=pd.read_csv(url1,index_col=None)
k=0
#tt['Date'] = tt['Date'].astype('datetime64[ns]')
#tt['Date'] = tt['Date'].apply(pd.to_datetime)
tt=tt.replace(['No Flex','Sold out','LOS2'],0) 

y=2020
#x=2019
arrival=tt['Date']

############################################################
tt['Datetime']=datetime.datetime.now()
dates=tt['Datetime']
for i in range(0,len(dates)):
    dates.at[i]=dates.loc[i]+datetime.timedelta(hours=i)
############################################################
tt['Date']=tt['Datetime']
tt=tt.drop(['Datetime','P(0) Value','P(1) Value'],axis=1)
#============================================================#
# ranges
#0000 to 0300 hrs=====>f1
#0301 to 0600 hrs=====>f2
#0601 to 0900 hrs=====>f3
#0901 to 1200 hrs=====>f4
#1201 to 1500 hrs=====>f5
#1501 to 1800 hrs=====>f6
#1801 to 2100 hrs=====>f7
#2101 to 2400 hrs=====>f8
#=============================================================#

f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
f7=0
f8=0

for i in range(0,len(dates)):
    tim=dates[i].time()
    if 00<=tim.hour<=3:
        f1+=1
    elif 3<tim.hour<=6:
        f2+=1
    elif 6<tim.hour<=9:
        f3+=1
    elif 9<tim.hour<=12:
        f4+=1
    elif 12<tim.hour<=15:
        f5+=1
    elif 15<tim.hour<=18:
        f6+=1
    elif 18<tim.hour<=21:
        f7+=1
    elif 21<tim.hour<=24:
        f8+=1

f1=f1/90.00
f2=f2/90.00
f3=f3/90.00
f4=f4/90.00
f5=f5/90.00
f6=f6/90.00
f7=f7/90.00
f8=f8/90.00

def price(tt,B,i,j,k,f1,f2,f3,f4,f5,f6,f7,f8):
    minus=tt.iloc[[i],[k]].values.astype(int)-tt.iloc[[i],[j]].values.astype(int)
    p0=(B-minus)/(10.0)
    dates=tt['Date']
    tim=dates[i].time()
    if 00<=tim.hour<=3:
        return p0*f1
    elif 3<tim.hour<=6:
        return p0*f2
    elif 6<tim.hour<=9:
        return p0*f3
    elif 9<tim.hour<=12:
        return p0*f4
    elif 12<tim.hour<=15:
        return p0*f5
    elif 15<tim.hour<=18:
        return p0*f6
    elif 18<tim.hour<=21:
        return p0*f7
    elif 21<tim.hour<=24:
        return p0*f8


def calc(B_B,arrival,tt):
    p_0=[]
    for i in range(0,len(arrival)):
        pp0=[]
        for k in range(4,9):
            
            for B in B_B:
                pp0.extend(price(tt,B,i,3,k,f1,f2,f3,f4,f5,f6,f7,f8))
        ppp0=max(pp0).astype('float32')
        p_0.extend(ppp0)
    p_0=np.asarray(p_0)
    np.round_(p_0,out=p_0)
    return p_0.astype(int)


P_0=[25,35,40,35,70]
P_1=[15,25,30,25,60]
tt['P(0) Value']=calc(P_0,arrival,tt) 
tt['P(1) Value']=calc(P_1,arrival,tt) 
pdf=tt
col=[2,3,4,5,6,7,8,9,10,11,12,13]
pdf=pdf.drop(pdf.columns[col],axis=1)
#tt.to_csv("task.csv",encoding='utf-8',index=None)


##p(1)A<B-15<C-25<E-30<F-25<G-60    
##pp=np.asarray(pp)
##pdd=['P('+str(x)+')' for x in ppp] 
##ppp=pd.DataFrame(ppp,columns=['P Value'])
#===================================================================================#
#===================================================================================#
#===================================================================================#          
#if Hotel_Big_Data.loc[i,'ibis budget Sydney Airport']==p_0:
#dec=datetime.date(x,12,1);
#week=q.strftime("%a")
#dec1=datetime.date(x,12,31);
#mini=min(tt['Date'])
#maxi=max(tt['Date'])
#dec2=pd.date_range(start=mini,end=maxi)
#dc=dec2.strftime("%#d/%#m/%Y").tolist()
#dcwk=dec2.strftime("%A").tolist()
#dcdd=dec2.strftime("%#W").tolist()
#dcmt=dec2.strftime("%B").tolist() 
#same=np.zeros(len(dc)).astype(int)
#one=np.zeros(len(dc)).astype(int)
#two=np.zeros(len(dc)).astype(int)
#three=np.zeros(len(dc)).astype(int)
#four=np.zeros(len(dc)).astype(int)
#five=np.zeros(len(dc)).astype(int)
#six=np.zeros(len(dc)).astype(int)
#seven=np.zeros(len(dc)).astype(int)
#one_week=np.zeros(len(dc)).astype(int)
#two_week=np.zeros(len(dc)).astype(int)
#remaining=np.zeros(len(dc)).astype(int)
#
#data_tr=zip(dcwk,dcmt,dcdd,dc,same,one,two,three,four,five,six,seven,one_week,two_week,remaining) 
#df=DataFrame.from_records(data_tr)  
#same=np.zeros(len(dc))                      
#df.columns=['WeekDay','Month','WeekNumber','Date of arrival','Same day','One day out','Two days out','Three days out','Four days out','Five days out','Six days out','Seven days out','One week out','Two weeks out','remaining period']
#p0_data=[]
#try:
#    for i in range(0,len(tt['Day'])):
#        rate=tt.loc[[i],['ibis budget Sydney Airport']].astype(int)
#        rate=rate.iloc[0]
#        rate=max(rate)
#        date=tt.loc[[i],['Date']]
#        date=date.iloc[0]
#        date=max(date)
#        date=datetime.datetime.strptime(date,'%d/%m/%Y')
#        date=date.date()
#        date1=date.strftime("%#d/%#m/%Y")
#        B1=df.loc[df['Date of arrival']==date1].index.values.astype(int)
#        if tt.loc[i,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Same day']=df.loc[B1,'Same day']+1
#        else:
#            continue
#        if tt.loc[i+1,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'One day out']=df.loc[B1,'One day out']+1            
#        else:
#            continue
#        if tt.loc[i+2,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Two days out']=df.loc[B1,'Two days out']+1
#        else:
#            continue
#        if tt.loc[i+3,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Three days out']=df.loc[B1,'Three days out']+1
#        else:
#            continue
#        if tt.loc[i+4,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Four days out']=df.loc[B1,'Four days out']+1
#        else:
#            continue
#        if tt.loc[i+5,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Five days out']=df.loc[B1,'Five days out']+1
#        else:
#            continue
#        if tt.loc[i+6,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Six days out']=df.loc[B1,'Six days out']+1
#        else:
#            continue
#        if tt.loc[i+7,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Seven days out']=df.loc[B1,'Seven days out']+1
#        else:
#            continue
#        if tt.loc[i+8,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'One week out']=df.loc[B1,'One week out']+1
#        else:
#            continue
#        if tt.loc[i+14,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'Two weeks out']=df.loc[B1,'Two weeks out']+1
#        else:
#            continue
#        if tt.loc[i+21,'ibis budget Sydney Airport']==p_0:
#                    df.at[B1,'remaining period']=df.loc[B1,'remaining period']+1
#        else:
#            continue
#except:
#    pass





















