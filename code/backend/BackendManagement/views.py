from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny


from BackendManagement.serializers import *
from BackendManagement.models import MyUser


class SalerViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_saler=True)
    serializer_class = SalerListSerializer
    http_method_names = ['get']


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
    http_method_names = ['get']


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
