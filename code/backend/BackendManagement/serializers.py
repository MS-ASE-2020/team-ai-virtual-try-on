from rest_framework import serializers

from .models import Customer, Product, Saler

from django.contrib.auth.models import User

import decimal


class SalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saler
        fields = ('username', 'password', 'phone_number')
    
class SalerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saler
        fields = ('username', 'phone_number')
    
