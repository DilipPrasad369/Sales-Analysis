# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from textwrap import wrap

df=pd.read_csv('C:\\Users\HOME\Downloads\SalesRecords.csv')

print(df)
print(df.to_string())#to print/read the entire dataframe
print(df.info())

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#GRAPH NO-01
#Number of Units sold of each item type in a particular month and in a specific year.
df['month']=df['Order Date'].str[0:2]
df['month']
df['month'] = df['month'].replace("/","", regex=True)
df['month']=df['month'].astype('int')


df['year']=df['Order Date'].str[-4:]
df['year']=df['year'].astype('int')


df.info()

month_unique=df['month'].unique()
year_unique=df['year'].unique()
item_type_unique=df['Item Type'].unique()

dict6={}
total=0
for i in item_type_unique:
    total=0
    for j in range(1000):
        if df.loc[j]['month']==3 and df.loc[j]['year']==2017 and df.loc[j]['Item Type']==i:
            total+=df.loc[j]['Units Sold']
    dict6[i]=total
            
dict6        

key=list(dict6.keys())
val=list(dict6.values())

x=np.array(key)
y=np.array(val)


#fig=plt.figure(figsize=(0.5,0.5))
#axl=plt.subplot(1,1,1)

font1 = {'family':'sans-serif','color':'black','size':20} #html fonts
font2 = {'family':'sans-serif','color':'darkred','size':15} #html fonts

plt.barh(x,y,height=0.5)
plt.xlabel("Units Sold",fontdict=font2)
plt.ylabel("Item Type",fontdict=font2)
plt.title("M/Y=3/2017",fontdict=font1)


for i in range(len(key)):
    plt.text(val[i],i,val[i],va='center_baseline')


plt.show()
#-------------------------------------------------------------        

#-------------------------------------------------------------
#count of each country from the .csv file
country_list=df["Country"]

country_list_unique=df["Country"].unique()

dict1={}

count=0


for i in country_list_unique:
    count=0
    for j in country_list:
        if i==j:
            count+=1
    dict1[i]=count

dict1
#-------------------------------------------------------------

#-------------------------------------------------------------
#GRAPH NO-02
#Region Wise Profit - 2017
Region_list=df["Region"]

Region_list_unique=df["Region"].unique()

dict2={}


for i in Region_list_unique:
    count=0
    for j in Region_list:
        if i==j:
            count+=1
    dict2[i]=count

dict2

Region_list_unique=np.sort(Region_list_unique)
Region_list_unique

dict9={}

for i in Region_list_unique:
    total=0
    for j in range(1000):
        if df.loc[j]['year']==2017 and df.loc[j]['Region']==i:
            total+=df.loc[j]['Total Profit']
    dict9[i]=total

dict9
    
key=list(dict9.keys())
key
val=list(dict9.values())
val
vals=[]
for i in val:
    a=i/(10**7)
    a=round(a,4)
    vals.append(a)

keys=['\n'.join(wrap(i,12)) for i in key]
keys[1]='Australia\nand\nOceania'

font1 = {'family':'sans-serif','color':'black','size':20} #html fonts
font2 = {'family':'sans-serif','color':'darkred','size':15} #html fonts

plt.plot(keys,val,"o-")#displays line chart with all the points marked


plt.xlabel("Region",fontdict=font2)
plt.ylabel("Total Profit",fontdict=font2)
plt.title("Region Wise Profit - 2017",fontdict=font1)



for i in range(len(key)):
    plt.text(i,val[i],vals[i],va='bottom',ha='left')

scale_factor = 1.1

ymin, ymax = plt.ylim()

plt.ylim(ymin * scale_factor, ymax * scale_factor)

plt.grid()
plt.show()            





#-------------------------------------------------------------
#GRAPH NO-03
#Profit Comparison 2016 vs 2017
Region_list=df["Region"]

Region_list_unique=df["Region"].unique()

dict2={}


for i in Region_list_unique:
    count=0
    for j in Region_list:
        if i==j:
            count+=1
    dict2[i]=count

dict2

Region_list_unique=np.sort(Region_list_unique)
Region_list_unique

dict10={}
dict11={}

for i in Region_list_unique:
    total=0
    for j in range(1000):
        if df.loc[j]['year']==2016 and df.loc[j]['Region']==i:
            total+=df.loc[j]['Total Profit']
    dict10[i]=total

for i in Region_list_unique:
    total=0
    for j in range(1000):
        if df.loc[j]['year']==2017 and df.loc[j]['Region']==i:
            total+=df.loc[j]['Total Profit']
    dict11[i]=total

    


key1=list(dict10.keys())
key1
val1=list(dict10.values())
val1
vals1=[]
for i in val1:
    a=i/(10**7)
    a=round(a,4)
    vals1.append(a)

keys1=['\n'.join(wrap(i,12)) for i in key]
keys1[1]='Australia\nand\nOceania'
    

key2=list(dict11.keys())
key2
val2=list(dict11.values())
val2
vals2=[]
for i in val2:
    a=i/(10**7)
    a=round(a,4)
    vals2.append(a)

keys2=['\n'.join(wrap(i,12)) for i in key]
keys2[1]='Australia\nand\nOceania'


font1 = {'family':'sans-serif','color':'black','size':20} #html fonts
font2 = {'family':'sans-serif','color':'darkred','size':15} #html fonts

keys1
keys2
val1
val2

plt.plot(keys1,val1,'o-')#displays line chart with all the points marked
plt.plot(keys2,val2,'o-')

plt.xlabel("Region",fontdict=font2)
plt.ylabel("Total Profit",fontdict=font2)
plt.title("Profit Comparison 2016 vs 2017",fontdict=font1)



for i in range(len(key1)):
    plt.text(i,val1[i],vals1[i],va='bottom',ha='left')



for i in range(len(key2)):
    plt.text(i,val2[i],vals2[i],va='bottom',ha='left')


scale_factor = 1.1

ymin, ymax = plt.ylim()

plt.ylim(ymin * scale_factor, ymax * scale_factor)

plt.legend(["2016","2017"])

plt.grid()
plt.show()       


     
#-------------------------------------------------------------

#-------------------------------------------------------------
#count of item types from the .csv file
item_list=df["Item Type"]

item_list_unique=df["Item Type"].unique()

dict3={}


for i in item_list_unique:
    count=0
    for j in item_list:
        if i==j:
            count+=1
    dict3[i]=count

dict3
#---------------------------------------------------------------------

#---------------------------------------------------------------------
#GRAPH NO-04
#Majority sale from which sales channel after evaluating whole data
#count of sales channel type from the .csv file
sales_channel_list=df["Sales Channel"]

sales_channel_list_unique=df["Sales Channel"].unique()

dict4={}


for i in sales_channel_list_unique:
    count=0
    for j in sales_channel_list:
        if i==j:
            count+=1
    dict4[i]=count

dict4

key=list(dict4.keys())
val=list(dict4.values())

plt.pie(val, labels=key ,explode =[0.1,0], shadow = True, autopct='%1.1f%%',colors=['#DE3163','#58D68D'])

plt.legend(title="Sales Channel")
plt.show()
#-------------------------------------------------------------

#-------------------------------------------------------------
#GRAPH NO-05
#Order priority share after evaluating the whole data
#count of order priority types from the .csv file
order_priority_list=df["Order Priority"]

order_priority_list_unique=df["Order Priority"].unique()

dict5={}


for i in order_priority_list_unique:
    count=0
    for j in order_priority_list:
        if i==j:
            count+=1
    dict5[i]=count

dict5

key=list(dict5.keys())
val=list(dict5.values())


plt.pie(val, labels=key , shadow = True, autopct='%1.1f%%')

plt.legend(title="Order Priority")
plt.show()
#-------------------------------------------------------------
#GRAPH N0-06
#Order priority share in a particular year
order_priority_list=df["Order Priority"]

order_priority_list_unique=df["Order Priority"].unique()

dict12={}


for i in order_priority_list_unique:
    count=0
    for j in range(1000):
        if df.loc[j]['year']==2017 and df.loc[j]['Order Priority']==i:
            count+=1
    dict12[i]=count

dict12

key=list(dict12.keys())
val=list(dict12.values())


plt.pie(val, labels=key , shadow = True, autopct='%1.1f%%')

plt.legend(title="Order Priority 2017")
plt.show()
#-------------------------------------------------------------
#GRAPH-07
#Monthly Profit of Year - 2010
#title=year(fix) , x-month , y-profit
#for a particular year sales profit for the 12-month.
dict7={}
total=0

month_unique=np.sort(month_unique)

for i in month_unique:
    total=0
    for j in range(100):
        if df.loc[j]['month']==i and df.loc[j]['year']==2010 :
            total+=df.loc[j]['Total Profit']
    dict7[i]=total
            
dict7
key=list(dict7.keys())
val=list(dict7.values())

vals=[]
for i in val:
    a=i/(10**6)
    a=round(a,4)
    vals.append(a)


font1 = {'family':'sans-serif','color':'black','size':20} #html fonts
font2 = {'family':'sans-serif','color':'darkred','size':15} #html fonts

plt.plot(key,val,"o-")#displays line chart with all the points marked
plt.xlabel("Month",fontdict=font2)
plt.ylabel("Total Profit",fontdict=font2)
plt.title("Monthly Profit of Year - 2010",fontdict=font1)



for i in range(len(key)):
    plt.text(i,val[i],vals[i],va='bottom',ha='left')

scale_factor = 1.1

ymin, ymax = plt.ylim()

plt.ylim(ymin * scale_factor, ymax * scale_factor)

plt.grid()
plt.show()

#-------------------------------------------------------------

#-----------------------------------------------------------------
#GRAPH-08
#online and offline presence in the market for a particular year
channel_unique=df['Sales Channel'].unique()
dict8={}
for i in channel_unique:
    count=0
    for j in range(1000):
        if df.loc[j]['year']==2015 and df.loc[j]['Sales Channel']==i:
            count+=1
    dict8[i]=count

dict8          


key=list(dict8.keys())
val=list(dict8.values())



plt.pie(val, labels=key , shadow = True, autopct='%1.1f%%')

plt.legend(title="Sales Channel")
plt.show()

#-------------------------------------------------------------------








