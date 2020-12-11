from rest_framework import serializers
from fluent_comments.models import FluentComment
from drf_haystack.serializers import HaystackSerializer
from django.contrib.auth import authenticate

from .search_indexes import ProductIndex
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
    

class SalerLoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        saler = authenticate(name=attrs['name'], password=attrs['password'])
        if not saler or not saler.is_saler:
            raise serializers.ValidationError(
                'Saler not exists or password is wrong.')
        return {'saler': saler}


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


class CustomerLoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        customer = authenticate(name=attrs['name'], password=attrs['password'])
        if not customer or customer.is_saler:
            raise serializers.ValidationError('Customer not exists or password is wrong.')
        return {'customer': customer}


class ProductSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

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
            'pics',
            'comments'
        )
    def get_comments(self, obj):
        product_comment = FluentComment.objects.filter(object_pk=obj.id, parent_id=None)
        serializer = CommentSerializer(product_comment, many=True)
        return serializer.data


class TryonSerializer(serializers.Serializer):
    url = serializers.CharField()

    class Meta:
        fields = ('url')


class ProductSearchSerializer(HaystackSerializer):

    class Meta:
        index_classes = [ProductIndex]
        fields = ('id', 'name', 'price', 'pics')


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = FluentComment
        fields = (
            'comment',
            'id',
            'user_id',
            'children',
            'submit_date'
        )
