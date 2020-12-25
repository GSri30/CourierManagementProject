"""CourierManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import Courier.views 
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Courier.views.Home.as_view(),name='home'),
    path('add/',Courier.views.AddCourier,name='add'),
    path('search/',Courier.views.SearchCourier.as_view(),name='search'),
    path('search/<slug:pk>',Courier.views.PostSpecific.as_view(),name='specific'),
    path('search/<slug:pk>/edit/',Courier.views.EditCourier,name='edit'),
    path('search/<slug:pk>/handover/',Courier.views.HandOver,name='handover'),
    path('search/<slug:pk>/delete/',Courier.views.DeleteCourier,name='delete'),
    #...users...
    path('login/',users.views.LoginView,name='login'),
    path('register/',users.views.RegisterView,name='register'),
    path('logout/',users.views.LogoutView,name='logout')
]