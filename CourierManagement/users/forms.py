from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import fields

class RegisterForm(UserCreationForm):
    #DiscordURL=forms.CharField(max_length=150,required=True,label="Discord URL",widget= forms.TextInput(attrs={'placeholder':'Discord Webhook Url'}))

    class Meta:
        model=User
        fields=[
            'username',
            'password1',
            'password2',
        ]
    
    # def save(self,commit=True):
    #     user=super(RegisterForm,self).save(commit=False)
    #     user.DiscordURL=self.cleaned_data["DiscordURL"]
    #     if commit:
    #         user.save()
    #     return user