from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView 
from rest_framework.response import Response 
import pandas as pd


a=pd.read_csv('G:\BACKedUP.csv')

date_list= a['Date'].to_list()
close_list= a['Close Price'].to_list()
open_list= a['Open Price'].to_list()
low_list= a['Low Price'].to_list()
high_list= a['High Price'].to_list()
change_percent=a['Spread Close-Open'].to_list()
   
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
        


onemonth_date=[]
for i in range(732,len(date_list)):
    onemonth_date.append(date_list[i])

onemonth_close=[]
for i in range(732,len(date_list)):
    onemonth_close.append(close_list[i])


post=[{
    'name':'RELIANCE',
    'work':'NSE'

},{
    'name':'TCS',
    'work':'NSE'


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