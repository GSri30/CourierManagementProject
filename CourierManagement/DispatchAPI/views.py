from rest_framework import permissions,generics,status
from .serializers import EmailMappingSerializer, MobileNumberMappingSerializer, PostSerializer
from .models import EmailMapping, MobileNumberMapping
from Courier.models import Post
from .permissions import IsMappingOwner
from django.conf import settings
from rest_framework.response import Response

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text
from .tokens import VerifyTokenUtil
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import send_mail


'''
Email Mappings
'''

'''
List of all Email Mappings
'''
class EmailMappingViewSet(generics.ListCreateAPIView):
    queryset=EmailMapping.objects.all()
    serializer_class=EmailMappingSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        query_set=super(EmailMappingViewSet,self).get_queryset()
        return query_set.filter(ParentMail=self.request.user.email)

    def post(self,request,*args,**kwargs):
        
        serializer = EmailMappingSerializer(data=request.data, context={'request': request})
        NumberOfChildren=EmailMapping.objects.filter(ParentMail__iexact=request.user.email)
        

        if serializer.is_valid(raise_exception=True):
            
            if NumberOfChildren.count() >= settings.MAX_CHILD_MAILS:
                return Response({"error":"max-limit-exceeded"},status=status.HTTP_400_BAD_REQUEST)
            
            if request.user.email == request.data['ChildMail']:
                return Response({"error":"circular-parent-child"},status=status.HTTP_400_BAD_REQUEST)

            mapping = serializer.save()

            token=VerifyTokenUtil.GeneratePassword()
            mapping.Verified=False
            mapping.ParentMail=request.user.email
            mapping.HashedPassword=VerifyTokenUtil.Hash(token)
            mapping.save()
        
            current_site = get_current_site(request)
            
            print(f"{current_site.domain}/api/verify/{settings.MAIL_PREFIX}/{mapping.id}/{token} is sent to {mapping.ChildMail}")
            
            # message = render_to_string('verification_emailmapping_mail.html', {
            #                 'mapping': mapping,
            #                 'prefix' : settings.MAIL_PREFIX,
            #                 'domain': current_site.domain,
            #                 'token': token,
            #                 'admin_contact' : 'zense@iiitb.ac.in'
            #             })
            # mail_subject='Activate your account for IIITB Dispatch'
            # to_email=mapping.ChildMail
            # send_mail(mail_subject,'',settings.EMAIL_HOST_USER,[to_email],html_message=message)
            
            if mapping:
                details = serializer.data
                return Response(details, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
Email Mapping with the specified id
'''
class EmailMappingSpecific(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmailMapping.objects.all()
    serializer_class=EmailMappingSerializer
    permission_classes=[permissions.IsAuthenticated,IsMappingOwner]
    http_method_names=['get','delete']
    lookup_field='id'




'''
Mobile Number Mappings
'''

'''
List of all Mobile Number Mappings
'''
class MobileNumberViewSet(generics.ListCreateAPIView):
    queryset=MobileNumberMapping.objects.all()
    serializer_class=MobileNumberMappingSerializer
    permission_classes=[permissions.IsAuthenticated,]

    def get_queryset(self):
        query_set=super(MobileNumberViewSet,self).get_queryset()
        return query_set.filter(ParentMail=self.request.user.email)

    def post(self,request,*args,**kwargs):
    
        serializer = MobileNumberMappingSerializer(data=request.data, context={'request': request})
        NumberOfChildren=MobileNumberMapping.objects.filter(ParentMail__iexact=request.user.email)
        
        if serializer.is_valid(raise_exception=True):
            
            if NumberOfChildren.count() >= settings.MAX_CHILD_MOBILE_NUMBERS:
                return Response({"error":"max-limit-exceeded"},status=status.HTTP_400_BAD_REQUEST)
            
        
            mapping = serializer.save()

            token=VerifyTokenUtil.GeneratePassword()
            mapping.Verified=False
            mapping.ParentMail=request.user.email
            mapping.HashedPassword=VerifyTokenUtil.Hash(token)
            mapping.save()
        
            current_site = get_current_site(request)
            
            print(f"{current_site.domain}/api/verify/{settings.MOBILE_PREFIX}/{mapping.id}/{token} is sent to ?")
            
            # message = render_to_string('verification_emailmapping_mail.html', {
            #                 'mapping': mapping,
            #                 'prefix' : settings.MOBILE_PREFIX,
            #                 'domain': current_site.domain,
            #                 'token': token,
            #                 'admin_contact' : 'zense@iiitb.ac.in'
            #             })
            # mail_subject='Activate your account for IIITB Dispatch'
            # to_email=mapping.ChildMail
            # send_mail(mail_subject,'',settings.EMAIL_HOST_USER,[to_email],html_message=message)
            
            if mapping:
                details = serializer.data
                return Response(details, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Mobile Number mapping with a specified id
'''
class MobileMappingSpecific(generics.RetrieveUpdateDestroyAPIView):
    queryset=MobileNumberMapping.objects.all()
    serializer_class=MobileNumberMappingSerializer
    permission_classes=[permissions.IsAuthenticated,IsMappingOwner]
    http_method_names=['get','delete']
    lookup_field='id'



'''
Post
'''

'''
List of couriers
'''
class PostViewSet(generics.ListAPIView):
    queryset=Post.objects.all().order_by('-CourierId')
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated,]
    http_method_names=['get','head','options']

'''
Courier with a specified id
'''
class PostDetailViewSet(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=['get','head','options']
    lookup_field='CourierId'

    def get_queryset(self):
        # Get the CourierId in url from self.kwargs
        query_set=super(PostDetailViewSet,self).get_queryset()
        return query_set.filter(CourierId=self.kwargs.get(self.lookup_field))




'''
Verifies the specified endpoint
'''

def verify(request,prefix,mappingId,token):
    if request.method=="GET":
        try:
            if prefix==settings.MAIL_PREFIX:
                mapping = EmailMapping.objects.get(id=mappingId)
            elif prefix==settings.MOBILE_PREFIX:
                mapping = MobileNumberMapping.objects.get(id=mappingId)
            else:
                raise Exception('invalid')
        except(TypeError, ValueError, OverflowError, Exception):
            mapping = None
        if mapping is not None and not mapping.Verified and VerifyTokenUtil.Match(token,mapping.HashedPassword):
            mapping.Verified = True
            mapping.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')