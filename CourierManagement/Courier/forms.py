from django import forms
from .models import Post

class NewCourier(forms.ModelForm):
    FromName=forms.CharField(max_length=100,label='From Name',widget= forms.TextInput(attrs={'placeholder':'Amazon,Flipkart'}))
    StudentName=forms.CharField(max_length=50,label="Student Name",widget= forms.TextInput(attrs={'placeholder':'Student Name'}))
    RollNumber=forms.CharField(required=False,max_length=50,label='Roll Number',widget= forms.TextInput(attrs={'placeholder':'Roll Number'}))
    Email=forms.EmailField(required=False,max_length=50,label='Email',widget= forms.TextInput(attrs={'placeholder':'Email ID'}))
    Mobile=forms.CharField(required=False,max_length=15,label='Mobile Number',widget= forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    PODnumber=forms.CharField(max_length=50,label='POD number',widget= forms.TextInput(attrs={'placeholder':'POD Number'}))
    OtherInformation=forms.CharField(required=False,max_length=100,label='Other',widget= forms.Textarea(attrs={'placeholder':'Additional Comments'}))
    
    class Meta:
        model=Post
        fields=[
            'FromName',
            'StudentName',
            'RollNumber',
            'Email',
            'Mobile',
            'PODnumber',
            'OtherInformation'
        ]


class UpdateCourier(forms.ModelForm):
    FromName=forms.CharField(max_length=100,label='From Name',widget= forms.TextInput(attrs={'placeholder':'Amazon,Flipkart'}))
    StudentName=forms.CharField(max_length=50,label="Student Name",widget= forms.TextInput(attrs={'placeholder':'Student Name'}))
    RollNumber=forms.CharField(required=False,max_length=50,label='Roll Number',widget= forms.TextInput(attrs={'placeholder':'Roll Number'}))
    Email=forms.EmailField(required=False,max_length=50,label='Email',widget= forms.TextInput(attrs={'placeholder':'Email ID'}))
    Mobile=forms.CharField(required=False,max_length=15,label='Mobile Number',widget= forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    PODnumber=forms.CharField(max_length=50,label='POD number',widget= forms.TextInput(attrs={'placeholder':'POD Number'}))
    OtherInformation=forms.CharField(required=False,max_length=100,label='Other',widget= forms.Textarea(attrs={'placeholder':'Additional Comments'}))
    
    class Meta:
        model=Post
        fields=[
            'FromName',
            'StudentName',
            'RollNumber',
            'Email',
            'Mobile',
            'PODnumber',
            'OtherInformation'
        ]

class HandOverForm(forms.ModelForm):
    RollNumber=forms.CharField(max_length=50,label='Roll Number',widget= forms.TextInput(attrs={'placeholder':'Roll Number'}))
    Email=forms.EmailField(required=False,max_length=50,label='Email',widget= forms.TextInput(attrs={'placeholder':'Email ID'}))
    Mobile=forms.CharField(max_length=15,label='Mobile Number',widget= forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    OtherInformation=forms.CharField(required=False,max_length=100,label='Other',widget= forms.Textarea(attrs={'placeholder':'Additional Comments'}))
    Collected=forms.BooleanField(required=False)
    Collected_On=forms.DateTimeField(required=False)

    class Meta:
        model=Post
        fields=[
            'RollNumber',
            'Email',
            'Mobile',
            'OtherInformation',
            'Collected',
            'Collected_On'
        ]