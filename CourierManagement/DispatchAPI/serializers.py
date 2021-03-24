from rest_framework import serializers
from .models import EmailMapping, MobileNumberMapping
from Courier.models import Post

class EmailMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailMapping
        fields=('id','ParentMail','ChildMail','HashedPassword','Verified')
        read_only_fields=('id','ParentMail','HashedPassword','Verified')

class MobileNumberMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=MobileNumberMapping
        fields=('id','ParentMail','ChildNumber','HashedPassword','Verified')
        read_only_fields=('id','ParentMail','HashedPassword','Verified')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('CourierId','FromName','StudentName','Email','Mobile','RollNumber','PODnumber','Received_On','OtherInformation','Notified','Collected','Collected_On')