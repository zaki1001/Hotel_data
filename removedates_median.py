# -*- coding: utf-8 -*-
"""
Created on Mon Apr 08 16:43:41 2019
@author: Zaki
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import datetime
from pandas import DataFrame
import re
import os
url="LowSeason.csv"  
lo = pd.read_csv(url,index_col=None)
url1="HighSeason.csv"
hi=pd.read_csv(url1,index_col=None)
#df=df.drop(['Unnamed: 0'],axis=1)
HighSeason=hi    
LowSeason=lo
loop=['Same day','One day out','Two days out','Three days out','Four days out','Five days out','Six days out','Seven days out','One week out','Two weeks out','remaining period']
loop_array=np.asarray(loop)
WeekName=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
WeekNames=pd.Series(['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'])
weeks=np.asarray(WeekName)
def remove1(df):
    while True:
        user=raw_input("Which Dates data you want removed?mm/dd/yyyy ")
        #arrival=raw_input("Which ArrivalStatus you want removed ")
    #import sys
        if len(user)>=8:
            try:
                try:
                    user2=datetime.datetime.strptime(user,'%m/%d/%Y')
                    user1=user2.strftime('%#m/%#d/%Y')
                    lll=df.loc[df['Date of arrival']==user1].index.values.astype(int)
                    df=df.drop(df.index[lll])
                except:
                    print("Wrong Date, Please Enter a valid Date ")
                    continue
            except:
                try:
                    user2=datetime.datetime.strptime(user,'%m-%d-%Y')
                    user1=user2.strftime('%#m/%#d/%Y')
                    lll=df.loc[df['Date of arrival']==user1].index.values.astype(int)
                    df=df.drop(df.index[lll])
                except:
                    print("Wrong Date, Please Enter a valid Date ")
                    continue
            break
        else:
            print("Wrong Input, Please Enter the correct format MM/DD/YYYY ")
            continue
    return df
def remove(df):
    while True:
        userinput=raw_input("Do you want to remove any more dates?y/n ")
        if userinput.lower()=='y' or userinput.lower()=='yes' or userinput.lower()=='yeah' or userinput.lower()=='yup':
            df=remove1(df)
            continue
        elif userinput.lower()=='n' or userinput.lower()=='no':
            break
        else:
            print("Wrong Input, Please Enter Y for Yes N for No")
            continue
    return df
  
for i in loop:
    j=i.replace(" ","_")
    king="low_"+str(j)
    exec "%s=lo[['Date of arrival','WeekDay',i]]" %(king)
for i in loop:
    j=i.replace(" ","_")
    king="high_"+str(j)
    exec "%s=hi[['Date of arrival','WeekDay',i]]" %(king)



while True:
    user=raw_input("Which season you want to remove dates from? Enter No to stop. ")
    if re.match("high",user.lower()):
            user1=raw_input("Which Arrival Status you want to remove it from ")
            if re.match("same",user1.lower()):
                high_Same_day=remove(high_Same_day)
            elif re.match("one",user1.lower()):
                high_One_day_out=remove(high_One_day_out)
            elif re.match("two",user1.lower()):
                high_Two_days_out=remove(high_Two_days_out)   
            elif re.match("three",user1.lower()):
                high_Three_days_out=remove(high_Three_days_out)
            elif re.match("four",user1.lower()):
                high_Four_days_out=remove(high_Four_days_out)
            elif re.match("five",user1.lower()):
                high_Five_days_out=remove(high_Five_days_out)
            elif re.match("six",user1.lower()):
                high_Six_days_out=remove(high_Six_days_out)
            elif re.match("seven",user1.lower()):
                high_Seven_days_out=remove(high_Seven_days_out)
            elif re.match("one week",user1.lower()):
                high_One_week_out=remove(high_One_week_out)
            elif re.match("two week",user1.lower()):
                high_Two_weeks_out=remove(high_Two_weeks_out)
            elif re.match("remaining",user1.lower()):
                high_remaining_period=remove(high_remaining_period)
            continue
    elif re.match("low",user.lower()):
            user1=raw_input("Which Arrival Status you want to remove it from ")
            if re.match("same",user1.lower()):
                low_Same_day=remove(low_Same_day)
            elif re.match("one",user1.lower()):
                low_One_day_out=remove(low_One_day_out)
            elif re.match("two",user1.lower()):
                low_Two_days_out=remove(low_Two_days_out)   
            elif re.match("three",user1.lower()):
                low_Three_days_out=remove(low_Three_days_out)
            elif re.match("four",user1.lower()):
                low_Four_days_out=remove(low_Four_days_out)
            elif re.match("five",user1.lower()):
                low_Five_days_out=remove(low_Five_days_out)
            elif re.match("six",user1.lower()):
                low_Six_days_out=remove(low_Six_days_out)
            elif re.match("seven",user1.lower()):
                low_Seven_days_out=remove(low_Seven_days_out)
            elif re.match("one week",user1.lower()):
                low_One_week_out=remove(low_One_week_out)
            elif re.match("two week",user1.lower()):
                low_Two_weeks_out=remove(low_Two_weeks_out)
            elif re.match("remaining",user1.lower()):
                low_remaining_period=remove(low_remaining_period) 
            continue
    elif re.match("no",user.lower()):
        break
def median(x):
    y=int(0.75*len(x))
    d=x[y]
    return d
def sortt(H1):
    H2=sorted(H1,reverse=True)
    H3=median(np.asarray(H2))
    return H3
import csv
with open('high_Same_day.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Same_day.loc[high_Same_day['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Same_day=pd.read_csv('high_Same_day.csv',index_col=None,header=None).transpose()
os.remove("high_Same_day.csv")   
with open('high_One_day_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_One_day_out.loc[high_One_day_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_One_day_out=pd.read_csv('high_One_day_out.csv',index_col=None,header=None).transpose()
os.remove("high_One_day_out.csv")     
with open('high_Two_days_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Two_days_out.loc[high_Two_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Two_days_out=pd.read_csv('high_Two_days_out.csv',index_col=None,header=None).transpose()
os.remove("high_Two_days_out.csv")     
with open('high_Three_days_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Three_days_out.loc[high_Three_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Three_days_out=pd.read_csv('high_Three_days_out.csv',index_col=None,header=None).transpose()
os.remove("high_Three_days_out.csv")     
with open('high_Four_days_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Four_days_out.loc[high_Four_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Four_days_out=pd.read_csv('high_Four_days_out.csv',index_col=None,header=None).transpose()
os.remove("high_Four_days_out.csv")      
with open('high_Five_days_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Five_days_out.loc[high_Five_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Five_days_out=pd.read_csv('high_Five_days_out.csv',index_col=None,header=None).transpose()
os.remove("high_Five_days_out.csv")       
with open('high_Six_days_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Six_days_out.loc[high_Six_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Six_days_out=pd.read_csv('high_Six_days_out.csv',index_col=None,header=None).transpose()  
os.remove("high_Six_days_out.csv")     
with open('high_Seven_days_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Seven_days_out.loc[high_Seven_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Seven_days_out=pd.read_csv('high_Seven_days_out.csv',index_col=None,header=None).transpose()
os.remove("high_Seven_days_out.csv")     
with open('high_One_week_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_One_week_out.loc[high_One_week_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_One_week_out=pd.read_csv('high_One_week_out.csv',index_col=None,header=None).transpose()
os.remove("high_One_week_out.csv")      
with open('high_Two_weeks_out.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_Two_weeks_out.loc[high_Two_weeks_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_Two_weeks_out=pd.read_csv('high_Two_weeks_out.csv',index_col=None,header=None).transpose() 
os.remove("high_Two_weeks_out.csv")     
with open('high_remaining_period.csv','wb') as f:
    for i in WeekName:
        #king="high_One_day_out_"+str(i)
        king=sortt(high_remaining_period.loc[high_remaining_period['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
high_remaining_period=pd.read_csv('high_remaining_period.csv',index_col=None,header=None).transpose()
os.remove("high_remaining_period.csv")               
        
#sortt(H1)
HighSeason=high_Same_day.append([high_One_day_out,high_Two_days_out,high_Three_days_out,high_Four_days_out,high_Five_days_out,high_Six_days_out,high_Seven_days_out,high_One_week_out,high_Two_weeks_out,high_remaining_period]) 
HighSeason['Arrival Status']=loop
HighSeason=HighSeason.append([WeekNames])
file_name='HighSeasonMedian.csv'
HighSeason.to_csv(file_name, encoding='utf-8',index=None) 



with open('low_Same_day.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Same_day.loc[low_Same_day['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Same_day=pd.read_csv('low_Same_day.csv',index_col=None,header=None).transpose() 
os.remove("low_Same_day.csv")    
with open('low_One_day_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_One_day_out.loc[low_One_day_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_One_day_out=pd.read_csv('low_One_day_out.csv',index_col=None,header=None).transpose() 
os.remove("low_One_day_out.csv")     
with open('low_Two_days_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Two_days_out.loc[low_Two_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Two_days_out=pd.read_csv('low_Two_days_out.csv',index_col=None,header=None).transpose()    
os.remove("low_Two_days_out.csv")    
with open('low_Three_days_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Three_days_out.loc[low_Three_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Three_days_out=pd.read_csv('low_Three_days_out.csv',index_col=None,header=None).transpose() 
os.remove("low_Three_days_out.csv")    
with open('low_Four_days_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Four_days_out.loc[low_Four_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Four_days_out=pd.read_csv('low_Four_days_out.csv',index_col=None,header=None).transpose() 
os.remove("low_Four_days_out.csv")     
with open('low_Five_days_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Five_days_out.loc[low_Five_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Five_days_out=pd.read_csv('low_Five_days_out.csv',index_col=None,header=None).transpose()
os.remove("low_Five_days_out.csv")      
with open('low_Six_days_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Six_days_out.loc[low_Six_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Six_days_out=pd.read_csv('low_Six_days_out.csv',index_col=None,header=None).transpose()
os.remove("low_Six_days_out.csv")       
with open('low_Seven_days_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Seven_days_out.loc[low_Seven_days_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Seven_days_out=pd.read_csv('low_Seven_days_out.csv',index_col=None,header=None).transpose()
os.remove("low_Seven_days_out.csv")       
with open('low_One_week_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_One_week_out.loc[low_One_week_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_One_week_out=pd.read_csv('low_One_week_out.csv',index_col=None,header=None).transpose()  
os.remove("low_One_week_out.csv")   
with open('low_Two_weeks_out.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_Two_weeks_out.loc[low_Two_weeks_out['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_Two_weeks_out=pd.read_csv('low_Two_weeks_out.csv',index_col=None,header=None).transpose()
os.remove("low_Two_weeks_out.csv")      
with open('low_remaining_period.csv','wb') as f:
    for i in WeekName:
        #king="low_One_day_out_"+str(i)
        king=sortt(low_remaining_period.loc[low_remaining_period['WeekDay']==i].drop(['WeekDay','Date of arrival'],axis=1).values)
        writer =csv.writer(f)
        writer.writerow(king)
low_remaining_period=pd.read_csv('low_remaining_period.csv',index_col=None,header=None).transpose() 
os.remove("low_remaining_period.csv")           
        
LowSeason=low_Same_day.append([low_One_day_out,low_Two_days_out,low_Three_days_out,low_Four_days_out,low_Five_days_out,low_Six_days_out,low_Seven_days_out,low_One_week_out,low_Two_weeks_out,low_remaining_period]) 
LowSeason['Arrival Status']=loop
LowSeason=LowSeason.append([WeekNames])
file_name1='LowSeasonMedian.csv'
LowSeason.to_csv(file_name1, encoding='utf-8',index=None) 






       