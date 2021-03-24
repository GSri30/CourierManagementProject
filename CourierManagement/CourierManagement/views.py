from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


'''
Home view of API
'''

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Couriers' : reverse('couriers', request=request, format=format),
        'Email Mappings': reverse('email-mappings', request=request, format=format),
        'Mobile Number Mappings': reverse('mobile-number-mappings', request=request, format=format),
        'Users' : reverse('users', request=request, format=format),
    })