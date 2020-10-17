from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView 
from rest_framework.response import Response 
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics



a=pd.read_csv('BACKedUP.csv')

date_list= a['Date'].to_list()
close_list= a['Close Price'].to_list()
open_list= a['Open Price'].to_list()
low_list= a['Low Price'].to_list()
high_list= a['High Price'].to_list()
change_percent=a['Change(%)'].to_list()
   
oneyear_date=[]
for i in range(507,len(date_list)):
    oneyear_date.append(date_list[i])

oneyear_close=[]
for i in range(507,len(date_list)):
    oneyear_close.append(close_list[i])

oneyear_open=[]
for i in range(507,len(date_list)):
    oneyear_open.append(open_list[i])
    
oneyear_low=[]
for i in range(507,len(date_list)):
    oneyear_low.append(low_list[i])

oneyear_high=[]
for i in range(507,len(date_list)):
    oneyear_high.append(high_list[i])


oneyear_change=[]
for i in range(507,len(date_list)):
    oneyear_change.append(change_percent[i])        


onemonth_date=[]
for i in range(732,len(date_list)):
    onemonth_date.append(date_list[i])

onemonth_close=[]
for i in range(732,len(date_list)):
    onemonth_close.append(close_list[i])


x=a[["Open Price", "High Price" ,"Low Price","Total Shares"]].values
y=a["Close Price"].values

x_train, x_test,y_train,y_test = train_test_split(x,y, test_size=0.2 ,random_state=42)

model= LinearRegression()
model.fit(x_train,y_train)

post=[{
    'name':'RELIANCE',
    'work':'BSE'
}]

def home(request):
    context={

        'post':post
    }
    return render(request,'home.html' ,context)    

def about(request):
    return render(request,'about.html')

class HomeView(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'index.html') 
   
class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None):         
        labels = date_list
        chartLabel = "Price"
        chartdata = close_list
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data)   

def subnav(request):
    return render(request,'subnav.html')


class HomeView2(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'oneyear.html') 
   
class ChartData2(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None):         
        labels = oneyear_date
        chartLabel = "Price"
        chartdata = oneyear_close
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data) 


class HomeView3(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'onemonth.html') 
   
class ChartData3(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None):         
        labels = onemonth_date
        chartLabel = "Price"
        chartdata = onemonth_close
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data) 

def HistoricData(request):
    Historic_Table=[]
    for i in range(len(oneyear_date)):
        Historic_dict={}

        Historic_dict['Date']=oneyear_date[i]
        Historic_dict['Close_price']=oneyear_close[i]
        Historic_dict['High_Price']=oneyear_high[i]
        Historic_dict['Low_Price']=oneyear_low[i]
        Historic_dict['Open_Price']=oneyear_open[i]
        Historic_dict['change']=oneyear_change[i]

        Historic_Table.append(Historic_dict)

        context={"Historic_Table": Historic_Table}
    return render(request,'historic_table.html',context)      

def live(request):

    url=("https://economictimes.indiatimes.com/reliance-industries-ltd/stocks/companyid-13215.cms")
    r=requests.get(url)

    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')
    time=soup.find_all("div",class_="nse_d dateTime")
    a=[]
    for i in (time):
        try:
            b=i.find("span",class_="_date").text
            a.append(b)
        except:
            continue
    #print(a[0])  
    price=soup.find_all(class_="stockInfo hidden")
    live_price=[]
    for i in price:
        try:
            z=i.find(id="bseTradeprice").text
            live_price.append(z)
        except:
            continue
    #print(live_price)
    arrow=soup.find_all(class_="data")
    arr=[]
    for i in arrow:
        try:
            q=i.find(id="bsePercentChange").text
            arr.append(q)
        except:
            continue
    arr1=""
    for i in range(1,len(arr[0])-1):
        arr1=arr1+(arr[0][i])
    #print(arr1)
    down_arrow=""
    up_arrow=""
    if arr1[0]=="-":
        down_arrow = '-' 
    else:
        up_arrow = '+'


    volume=soup.find_all(class_="Volume")
    vol=[]
    for i in volume:
        try:
            w=i.find(id="bseVolume").text
            vol.append(w)
        except:
            continue
    #print(vol)
    openn=soup.find_all(class_="Openprice")
    open_price=[]
    prev_price=[]
    for i in openn:
        try:
            oo=i.find(id="bseOpenprice").text
            open_price.append(oo)
        except:
            continue
    #print(open_price)
    pre=soup.find_all(class_="Closeprice")
    for i in pre:
        try:
            pre=i.find(id="bseCloseprice").text
            prev_price.append(pre)
        except:
            continue
    #print(prev_price)

    context={
        "update":a[0],
        "live_price":live_price[0],
        "arrow":arr1,
        "up_arrow":up_arrow,
        "down_arrow":down_arrow,
        "volume":vol[0],
        "Open_price":open_price[0],
        "Prev_price":prev_price[0]    
    }
    return render(request,'live.html',context)   


#LINEAR REGRESSION

def prediction(request):
    
    url2=("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
    r2=requests.get(url2)

    htmlcontent2=r2.content

    soup2=BeautifulSoup(htmlcontent2,'html.parser')

    url=("https://economictimes.indiatimes.com/reliance-industries-ltd/stocks/companyid-13215.cms")
    r=requests.get(url)

    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')
    volume=soup.find_all(class_="Volume")
    volume_live=[]

    for i in volume:
        try:
            w=i.find(id="bseVolume").text
            temp=w.replace(',','')
            volume_live.append(temp)
        except:
            continue
    #print("VOlume",volume_live)



    live_low=[]
    low_soup=soup2.find_all("div",class_="clearfix lowhigh_band todays_lowhigh_wrap")
    #print(low_soup)
    for i in low_soup:
        try:
            lowprice_live=i.find(class_="low_high1").text
            #print(lowprice_live)
            live_low.append(lowprice_live)
        except:
            continue
    #print(live_low)
    live_low1=[]
    live_low1.append(live_low[0])
    #print("Low",live_low1)


    live_high=[]    
    high_soup=soup2.find_all("div",class_="clearfix lowhigh_band todays_lowhigh_wrap")
    for i in high_soup:
        try:
            highprice_live=i.find(class_="low_high3").text
            #print(highprice_live)
            #aa=highprice_live.find
            live_high.append(highprice_live)
        except:
            continue

    live_high1=[]
    live_high1.append(live_high[0])
    #print("High",live_high1)



    openn=soup.find_all(class_="Openprice")
    open_price=[]
    prev_close_price=[]
    for i in openn:
        try:
            oo=i.find(id="nseOpenprice").text
            #print(oo)
            open_price.append(oo)
        except:
            continue
    #print("OpenPrice",open_price)

    pre=soup.find_all(class_="Closeprice")
    for i in pre:
        try:
            pre=i.find(id="nseCloseprice").text
            #print(pre)
            prev_close_price.append(pre)
        except:
            continue
    #print("CLoseprice",prev_close_price)

    price=soup.find_all(class_="stockInfo")

    #print(price)
    live_price=[]


    for i in price:
        try:
            z=i.find(class_="value").text
            live_price.append(z)
        except:
            continue
    #print("Live Price",live_price)

    data_live = {'Open':open_price, 'High':live_high1, 'Low':live_low1, 'Volume':volume_live } 
  
    # Create DataFrame 
    live_df = pd.DataFrame(data_live) 
    ans=model.predict(live_df)

    ans1=ans.tolist()
    str_ans=(str(ans1[0]))

    lv=live_price[0]



    pred=""

    if str_ans > lv:
        pred = '+'

    context={
        "live_price":live_price[0],
        "High_price":live_high1[0],
        "Low_price":live_low1[0],
        "volume":volume_live[0],
        "Open_price":open_price[0],
        "Prev_price":prev_close_price[0],
        "answer":ans1[0],
        "pred":pred
    }
    return render(request,'prediction.html',context)














