from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView 
from rest_framework.response import Response 
import pandas as pd


a=pd.read_csv('G:\BACKedUP.csv')

date_list= a['Date'].to_list()
#print(date_list)
close_list= a['Close Price'].to_list()
#print(close_list)
open_list= a['Open Price'].to_list()
#print(open_list)
low_list= a['Low Price'].to_list()
high_list= a['High Price'].to_list()
#print(low_list)
#print(high_list)
change_percent=a['Spread Close-Open'].to_list()
# print(change_percent)    





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
        chartLabel = "my data"
        chartdata = close_list
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data)   

def subnav(request):
    return render(request,'subnav.html')
