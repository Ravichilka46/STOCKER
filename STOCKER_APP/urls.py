from django.contrib import admin
from django.urls import path,include
from STOCKER_APP import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('about', views.about,name="About"),
    path('chart', views.HomeView.as_view()), 
    path('api', views.ChartData.as_view()),
    
]