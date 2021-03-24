from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add/',AddCourier,name='add'),
    path('search/',SearchCourier.as_view(),name='search'),
    path('search/<slug:pk>',PostSpecific.as_view(),name='specific'),
    path('search/<slug:pk>/edit/',EditCourier,name='edit'),
    path('search/<slug:pk>/handover/',HandOver,name='handover'),
    path('search/<slug:pk>/delete/',DeleteCourier,name='delete'),
]
