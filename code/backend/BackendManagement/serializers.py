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
    # self_pics = serializers.ImageField()
    class Meta:
        model = MyUser
        extra_kwargs = {'password': {'write_only': True}, 'name': {'read_only': True}, 'is_saler': {'read_only': True}}
        fields = ('name', 'phone_number', 'password', 'is_saler', 'self_pics')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        extra_kwargs = {'id': {'read_only': True}}
        fields = (
            'id',
            'name',
            'price',
            'link',
            'number_people_scoring_one',
            'number_people_scoring_two',
            'number_people_scoring_three',
            'number_people_scoring_four',
            'number_people_scoring_five',
            'owned_saler',
            'pics'
        )
