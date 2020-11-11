import os
import shutil

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.conf import settings

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from BackendManagement.serializers import *
from BackendManagement.models import *


class SalerViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_saler=True)
    serializer_class = SalerListSerializer
    http_method_names = ['get', 'put']

    def list(self, request):
        queryset = MyUser.objects.filter(is_saler=True)
        serializer = SalerListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = MyUser.objects.filter(is_saler=True, pk=pk)
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Saler not exist'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = request.data.copy()
            if data.get('password'):
                data['password'] = make_password(data['password'])
                queryset.update(name=pk, password=data['password'])
            if data.get('phone_number'):
                queryset.update(name=pk, phone_number=data['phone_number'])
        except IntegrityError as e:
            return Response({'status': 'Internal Error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'status': 'Success', 'message': "Update the saler's info successfully"}, status.HTTP_200_OK)


class SalerSignupViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = SalerSerializer

    def create(self, request, *args):
        try:
            data = request.data.copy()
            data['password'] = make_password(data['password'])
            data['is_saler'] = 'true'
            serializer = SalerSerializer(data=data)
            serializer.is_valid(True)
            serializer.save()
            return Response('Successful create a new saler', status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_saler=False)
    serializer_class = CustomerListSerializer
    http_method_names = ['get', 'put']

    def list(self, request):
        queryset = MyUser.objects.filter(is_saler=False)
        serializer = CustomerListSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        customer = MyUser.objects.get(pk=pk, is_saler=False)
        data = request.data.copy()
        data['password'] = make_password(data['password']) if data.get('password') else customer.password
        data['phone_number'] = data['phone_number'] if data.get('phone_number') else customer.phone_number
        data['self_pics'] = data['self_pics'] if data.get('self_pics') else customer.self_pics
        if data.get('self_pics'):
            pics_path = os.path.join(settings.MEDIA_ROOT, 'customers', 'customer_' + str(customer))
            previous_pics = os.listdir(pics_path)
            for previous_pic in previous_pics:
                if os.path.join('customers', 'customer_' + str(customer), previous_pic) != data['self_pics']:
                    os.remove(os.path.join(pics_path, previous_pic))
        serializer = CustomerListSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', 'message': "Update the customer's info successfully"}, status.HTTP_200_OK)
        return Response({'status': 'Internal Error', 'message': "Failed to update customer information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerSignupViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer

    def create(self, request, *args):
        try:
            data = request.data.copy()
            data['password'] = make_password(data['password'])
            data['is_saler'] = 'false'
            serializer = CustomerSerializer(data=data)
            serializer.is_valid(True)
            serializer.save()
            return Response('Successful create a new customer', status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, pk=None):
        queryset = Product.objects.all()
        obj = get_object_or_404(queryset, pk=pk)

        try:
            obj.delete()
            shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'products', pk))
        except Exception as e:
            return Response({
                'status': 'Bad Request',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'status': 'Success',
            'message': 'Delete the Product Successfully'
        }, status=status.HTTP_200_OK)
