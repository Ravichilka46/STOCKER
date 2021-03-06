"""STOCKER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from STOCKER_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('STOCKER_APP.urls')),
    path('chart', views.HomeView.as_view()), 
    path('api', views.ChartData.as_view()),
    path('oneyear', views.HomeView2.as_view()), 
    path('api2', views.ChartData2.as_view()),
    path('onemonth', views.HomeView3.as_view()), 
    path('api3', views.ChartData3.as_view()),
]
