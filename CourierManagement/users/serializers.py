from django.db import models
from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUser
        fields=('id','username','name','email','password')
        write_only_fields=('password')
        

    def create(self,validated_data):
        user=AppUser.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(AppUserSerializer, self).update(instance, validated_data)

class AppUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUser
        fields=('id','username','name','email','password')
        read_only_fields=('id','username','email','password')

class AppUserPasswordUpdateSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)