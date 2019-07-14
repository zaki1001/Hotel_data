# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:07:55 2019

@author: Zaki
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import datetime
from pandas import DataFrame
#url="BookingsReportarnc.csv" #E:\\Thomas PPH\\test3\\
import os 
cw=os.getcwd()
print (cw)
dirs=os.listdir( cw )
print (dirs)

for file in dirs:
    if file.endswith("csv"):
        url=cw+'\\'+str(file)
        url1=cw+'\\'+"Thomas"+str(file)
print (url)
#df = pd.read_csv(url,index_col=None)
import csv
input=open(url,mode='r')
output=open(url1,mode='w',newline='')
writer=csv.writer(output)
for row in csv.reader(input):
    if any(field.strip() for field in row):
        writer.writerow(row)
input.close()
output.close()

#names=['Name','Company','Date Made','Check-in','Depart	Nights','Room No.','Type','Value','AvgRate','Sold By']
df1 = pd.read_csv(url1,index_col=None)
df2= pd.read_csv(url1,index_col=None,parse_dates=[2,3,4])
#os.remove(url1)
col=[1,-1]
df1=df1.drop(df1.columns[col],axis=1)
df1=df1.dropna(how='any',axis=0)
df2=df2.drop(df2.columns[col],axis=1)
df2=df2.dropna(how='any',axis=0)

mini=min(df2['Date Made'])
maxi=max(df2['Depart'])
dec2=pd.date_range(start=mini,end=maxi)
dc=dec2.strftime("%#m/%#d/%Y").tolist()
dcwk=dec2.strftime("%A").tolist()
dcdd=dec2.strftime("%#W").tolist()
dcmt=dec2.strftime("%B").tolist() 
same=np.zeros(len(dc)).astype(int)
one=np.zeros(len(dc)).astype(int)
two=np.zeros(len(dc)).astype(int)
three=np.zeros(len(dc)).astype(int)
four=np.zeros(len(dc)).astype(int)
five=np.zeros(len(dc)).astype(int)
six=np.zeros(len(dc)).astype(int)
seven=np.zeros(len(dc)).astype(int)
one_week=np.zeros(len(dc)).astype(int)
two_week=np.zeros(len(dc)).astype(int)
remaining=np.zeros(len(dc)).astype(int)

data_tr=zip(dcwk,dcmt,dcdd,dc,same,one,two,three,four,five,six,seven,one_week,two_week,remaining) 
df=DataFrame.from_records(data_tr)  
same=np.zeros(len(dc))                      
df.columns=['WeekDay','Month','WeekNumber','Date of arrival','Same day','One day out','Two days out','Three days out','Four days out','Five days out','Six days out','Seven days out','One week out','Two weeks out','remaining period']
df.to_csv("Hotel_Big_Data.csv",encoding='utf-8',index=None)
