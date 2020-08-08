from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView 
from rest_framework.response import Response 
   

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
        labels = [ 
            'January', 
            'February',  
            'March',  
            'April',  
            'May',  
            'June',  
            'July'
            ] 
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data)   
