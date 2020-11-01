from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny


from BackendManagement.serializers import SalerSerializer, SalerListSerializer
from BackendManagement.models import MyUser


class SalerViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = SalerListSerializer


class SalerSignupViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = SalerSerializer

    def create(self, request, *args):
        try:
            data = request.data.copy()
            data['password'] = make_password(data['password'])
            serializer = SalerSerializer(data=data)
            serializer.is_valid(True)
            serializer.save()
            return Response('Successful create a new saler', status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)