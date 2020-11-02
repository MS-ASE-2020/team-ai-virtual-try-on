from rest_framework import serializers

from .models import MyUser

import decimal


class SalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'password', 'phone_number', 'self_pics')
    

class SalerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'phone_number', 'is_saler', 'self_pics')
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'password', 'phone_number', 'self_pics')


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'phone_number', 'is_saler', 'self_pics')
