from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import Post
from .forms import NewCourier,UpdateCourier,HandOverForm
from django.contrib.admin.views.decorators import staff_member_required
from DispatchAPI.models import EmailMapping, MobileNumberMapping
from django.core.mail import send_mail


'''
Main view
'''

class Home(generic.base.TemplateView):
    template_name='index.html'


'''
Search View for a courier
'''

class SearchCourier(generic.ListView):
    queryset=Post.objects.order_by('-Received_On')
    template_name='search_courier.html'

'''
Specific view of a post
'''

class PostSpecific(generic.DetailView):
    model=Post
    template_name='post_specific.html'





'''
Adds new courier
'''

@login_required
@staff_member_required
def AddCourier(request):
    if request.method=="POST":
        form=NewCourier(request.POST or None)
        if form.is_valid():
            form.save()
            current=Post.objects.filter(
                    PODnumber=form.cleaned_data['PODnumber'],
                    StudentName=form.cleaned_data['StudentName'],
                    FromName=form.cleaned_data['FromName'],
                    Email=form.cleaned_data['Email'],
                    RollNumber=form.cleaned_data['RollNumber'],
                    Mobile=form.cleaned_data['Mobile'],
                    OtherInformation=form.cleaned_data['OtherInformation'],
                    )[0]
            messages.add_message(request,messages.INFO,current.getCourierId())
            #CurrentDT=datetime.now().strftime("%B %d, %Y")+" at "+datetime.now().strftime("%H:%M:%S")
            #DiscordWebhook.Notify(current.getCourierId(),current.getFromName(),current.getStudentName(),current.getRollNumber(),current.getEmail(),current.getMobile(),CurrentDT,current.getOtherInfo(),False)            
            notified=False
            email=current.getEmail()
            mobile=current.getMobile()
            
            if email:
                possibilities=EmailMapping.objects.filter(ParentMail__iexact=email)
                if possibilities.count()>0:
                    notified=True
                    #send_mail(current)
                    print(f"Send mail to {email}")
                else:
                    possibilities=EmailMapping.objects.filter(ChildMail__iexact=email)
                    if possibilities:
                        for possiblity in possibilities:
                            if possiblity.Verified:
                                notified=True
                                #send_mail(possiblity)
                                print(f"Sent mail to {possiblity.ParentMail}")
            
            if not notified and mobile:
                possibilities=MobileNumberMapping.objects.filter(ChildNumber__iexact=mobile)
                if possibilities:
                    for possiblity in possibilities:
                        if possiblity.Verified:
                            notified=True
                            #send_mail(possiblity)
                            print(f"Sent mail to {possiblity.ParentMail}")

            form.cleaned_data['Notified']=notified
            form.save()

            messages.success(request,"Courier has been added successfully!")
            if notified:
                messages.success(request,"Sent notification successfully!")
            else:
                messages.warning(request,"Couldn't send notification.")
            
            return HttpResponseRedirect('/')
        return render(request,"add_courier.html",{})
    else:
        form=NewCourier()
    return render(request,'add_courier.html',{'form':form})


'''
Allows admins to edit courier details
'''

@login_required
@staff_member_required
def EditCourier(request,pk,*args,**kwargs):
    CourierObj=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        UpdatedPost=UpdateCourier(request.POST,instance=CourierObj)
        if UpdatedPost.is_valid():
            UpdatedPost.save()
            messages.success(request,"Courier has been updated successfully!")
            messages.warning(request,"Changes are NOT notified.")
            return redirect('search')
    else:
        UpdatedPost=UpdateCourier(instance=CourierObj)
    return render(request,"edit_courier.html",{"original_post":CourierObj,"updated_post":UpdatedPost})

'''
Marks courier as received by student
'''

@login_required
@staff_member_required
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


'''
Deletes a Courier
'''

@login_required
@staff_member_required
def DeleteCourier(request,pk=None):
    post=Post.objects.get(CourierId=pk)
    post.delete()
    messages.success(request,"Courier has been deleted successfully!")
    return HttpResponseRedirect('/search')