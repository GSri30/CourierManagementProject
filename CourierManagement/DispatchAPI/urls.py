from django.urls import path
from .import views as DispatchViews

urlpatterns = [
    path('emailmappings/',DispatchViews.EmailMappingViewSet.as_view(),name='email-mappings'),
    path('emailmappings/<id>/',DispatchViews.EmailMappingSpecific.as_view(),name='email-mapping-specific'),
    path('mobilemappings/',DispatchViews.MobileNumberViewSet.as_view(),name='mobile-number-mappings'),
    path('mobilemappings/<id>/',DispatchViews.MobileMappingSpecific.as_view(),name='mobile-mapping-specific'),
    path('couriers/',DispatchViews.PostViewSet.as_view(),name='couriers'),
    path('couriers/<CourierId>/',DispatchViews.PostDetailViewSet.as_view(),name='courier-detail'),
    path('verify/<prefix>/<mappingId>/<token>/',DispatchViews.verify,name='verify'),
]
