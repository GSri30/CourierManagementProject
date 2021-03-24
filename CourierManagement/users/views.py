from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import permissions,generics,status
from .models import AppUser
from .serializers import AppUserPasswordUpdateSerializer, AppUserSerializer, AppUserUpdateSerializer
from .decorators import ifNotAuthenticated
from rest_framework.response import Response
from .permissions import IsOwner
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


'''
Login View
'''
@ifNotAuthenticated
def LoginView(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')    
        return render(request,"login.html",{"form":form})
    
    form=AuthenticationForm()
    return render(request,'login.html',{"form":form})


'''
Logout View
'''
def LogoutView(request):
    logout(request)
    return redirect('home')



'''
API
'''

'''
List of all Users
'''
class AppUserAPI(generics.ListCreateAPIView):

    queryset = AppUser.objects.all().order_by('-id')
    serializer_class = AppUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = AppUserSerializer(data=request.data, context={'request': request})
        same_mail_set=AppUser.objects.filter(email__iexact=request.data['email'])
        if serializer.is_valid(raise_exception=True):
    
            if(same_mail_set.count()>0):
                return HttpResponse("Mail is already registered.")
        
            user = serializer.save()
            
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            
            message = render_to_string('verification_mail.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.id)),
                            'token': account_activation_token.make_token(user),
                            'admin_contact' : 'zense@iiitb.ac.in'
                        })
            mail_subject='Activate your account for IIITB Dispatch'
            to_email=user.email
            #send_mail(mail_subject,'',settings.EMAIL_HOST_USER,[to_email],html_message=message)
            print("Mail sent.")
            
            if user:
                details = serializer.data
                return Response(details, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
Specific User View
'''

class AppUserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppUserUpdateSerializer
    queryset = AppUser.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    lookup_field = 'username'


'''
Updates a Specific User
'''

class AppUserUpdateAPI(generics.UpdateAPIView):

    serializer_class = AppUserPasswordUpdateSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = 'username'


    def put(self, request, *args, **kwargs):
        user = self.request.user
        serializer = AppUserPasswordUpdateSerializer(data=request.data)

        if serializer.is_valid():
            
            current_password=serializer.data.get("current_password")
            
            if not user.check_password(current_password):
                return Response({"current_password": ["Wrong password."]},status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
Activates/Verifies the specified endpoint
'''

def activate(request, uidb64, token):
    if request.method == "GET":
        User = get_user_model()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')