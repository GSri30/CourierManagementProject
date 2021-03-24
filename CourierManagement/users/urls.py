from django.urls import include,path
from .import views


urlpatterns = [
    path('users/',views.AppUserAPI.as_view(),name='users'),
    path('users/<username>/',views.AppUserDetailAPI.as_view(),name='user-detail'),
    path('users/<username>/reset-password/',views.AppUserUpdateAPI.as_view(),name='user-update'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
]
