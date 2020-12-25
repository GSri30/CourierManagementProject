from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import Post
from .forms import NewCourier,UpdateCourier,HandOverForm

from Discord.webhook import DiscordWebhook
from Discord.webhookURL import WEBHOOK_URL

class Home(generic.base.TemplateView):
    template_name='index.html'

@login_required
def AddCourier(request):
    if request.method=="POST":
        form=NewCourier(request.POST or None)
        if form.is_valid():
            form.save()
            current=Post.objects.filter(PODnumber=form.cleaned_data['PODnumber'],
                                        StudentName=form.cleaned_data['StudentName'],
                                        FromName=form.cleaned_data['FromName'],
                                        Email=form.cleaned_data['Email'],
                                        RollNumber=form.cleaned_data['RollNumber'],
                                        Mobile=form.cleaned_data['Mobile'],
                                        OtherInformation=form.cleaned_data['OtherInformation'],
                                        )[0]
            messages.add_message(request,messages.INFO,current.getCourierId())
            CurrentDT=datetime.now().strftime("%B %d, %Y")+" at "+datetime.now().strftime("%H:%M:%S")
            DiscordWebhook.Notify(current.getCourierId(),current.getFromName(),current.getStudentName(),current.getRollNumber(),current.getEmail(),current.getMobile(),CurrentDT,current.getOtherInfo(),False)            
            messages.success(request,"Courier has been added successfully!")
            messages.success(request,"Sent notification successfully!")
            return HttpResponseRedirect('/')
        return render(request,"add_courier.html",{})
    else:
        form=NewCourier()
    return render(request,'add_courier.html',{'form':form})

class SearchCourier(generic.ListView):
    queryset=Post.objects.order_by('-Received_On')
    template_name='search_courier.html'

class PostSpecific(generic.DetailView):
    model=Post
    template_name='post_specific.html'

@login_required
def EditCourier(request,pk,*args,**kwargs):
    CourierObj=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        UpdatedPost=UpdateCourier(request.POST,instance=CourierObj)
        if UpdatedPost.is_valid():
            UpdatedPost.save()
            CurrentDT=datetime.now().strftime("%B %d, %Y")+" at "+datetime.now().strftime("%H:%M:%S")
            DiscordWebhook.Notify(CourierObj.getCourierId(),CourierObj.getFromName(),CourierObj.getStudentName(),CourierObj.getRollNumber(),CourierObj.getEmail(),CourierObj.getMobile(),CurrentDT,CourierObj.getOtherInfo(),True)
            messages.success(request,"Courier has been updated successfully!")
            messages.success(request,"Sent notification successfully!")
            return redirect('search')
    else:
        UpdatedPost=UpdateCourier(instance=CourierObj)
    return render(request,"edit_courier.html",{"original_post":CourierObj,"updated_post":UpdatedPost})

@login_required
def HandOver(request,pk,*args,**kwargs):
    ExistingObj=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        UpdatedObj=HandOverForm(request.POST,instance=ExistingObj)
        if UpdatedObj.is_valid():
            ExistingObj.Collected=True
            ExistingObj.Collected_On=datetime.now()
            UpdatedObj.save()
            messages.success(request,"Courier has been updated successfully!")
            return redirect('home')
    else:
        UpdatedObj=HandOverForm(instance=ExistingObj)
    return render(request,"hand_over.html",{"existing_post":ExistingObj,"updated_post":UpdatedObj})

@login_required
def DeleteCourier(request,pk=None):
    post=Post.objects.get(CourierId=pk)
    post.delete()
    messages.success(request,"Courier has been deleted successfully!")
    return HttpResponseRedirect('/search')