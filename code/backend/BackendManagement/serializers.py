from rest_framework import serializers

from .models import MyUser, Product

import decimal


class SalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('name', 'password', 'phone_number', 'is_saler')
    

class SalerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        extra_kwargs = {'password': {'write_only': True}, 'name': {'read_only': True}, 'is_saler': {'read_only': True}}
        fields = ('name', 'phone_number', 'password', 'is_saler')
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('name', 'password', 'phone_number', 'self_pics', 'is_saler')


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        extra_kwargs = {'password': {'write_only': True}, 'name': {'read_only': True}, 'is_saler': {'read_only': True}}
        fields = ('name', 'phone_number', 'password', 'is_saler', 'self_pics')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'link', 'overall_score', 'number_people_scoring', 'owned_saler', 'pics')
