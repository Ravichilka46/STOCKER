from django.contrib import admin
from django.urls import path,include
from STOCKER_APP import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('about', views.about,name="About"),
    path('subnav', views.subnav,name="Subnav"),
    path('Historic_table', views.HistoricData,name="Historic_table"),
    path('live', views.live,name="Live"),
    path('prediction', views.prediction,name="Prediction"),
    path('chart', views.HomeView.as_view()), 
    path('api', views.ChartData.as_view()),
    path('oneyear', views.HomeView2.as_view()), 
    path('api2', views.ChartData2.as_view()),
    path('onemonth', views.HomeView3.as_view()), 
    path('api3', views.ChartData3.as_view()),
]