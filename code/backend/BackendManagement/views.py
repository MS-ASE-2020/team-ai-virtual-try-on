import os
import shutil

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.conf import settings

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from BackendManagement.serializers import *
from BackendManagement.models import *
from BackendManagement.permissions import IsOwner

from TryonModel.test import tryon


class SalerViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_saler=True)
    serializer_class = SalerListSerializer
    permission_classes = (IsOwner,)
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


class SalerLoginViewSet(viewsets.GenericViewSet):
    serializer_class = SalerLoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def login(self, request):
        serializer = SalerLoginSerializer(data=request.data.copy())
        if serializer.is_valid(raise_exception=True):
            saler = serializer.validated_data['saler']
            login(request, saler)
            response = Response(SalerListSerializer(saler).data)
            response.set_cookie('saler_name', saler.name)
            return response
        return Response({
            'status': 'Internal Error',
            'message': 'Failed to login.'
        }, status.HTTP_500_INTERNAL_SERVER_ERROR)


class SalerLogoutViewSet(APIView):
    http_method_names = ['get']

    def get(self, request, *args):
        # print(request.user.is_anonymous)
        if not request.user.is_anonymous:
            logout(request)
            return Response('Logout successfully', status.HTTP_200_OK)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Not login yet'
            }, status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_saler=False)
    serializer_class = CustomerListSerializer
    permission_classes = (IsOwner,)
    http_method_names = ['get', 'put']

    def list(self, request):
        queryset = MyUser.objects.filter(is_saler=False)
        serializer = CustomerListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        customer = self.get_object()
        serializer = self.get_serializer(customer)
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


class CustomerLoginViewSet(viewsets.GenericViewSet):
    serializer_class = CustomerLoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def login(self, request):
        serializer = CustomerLoginSerializer(data=request.data.copy())
        if serializer.is_valid(raise_exception=True):
            customer = serializer.validated_data['customer']
            login(request, customer)
            response = Response(CustomerListSerializer(customer).data)
            response.set_cookie('customer_name', customer.name)
            return response
        return Response({
            'status': 'Internal Error',
            'message': 'Failed to login.'
        }, status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerLogoutViewSet(APIView):
    http_method_names = ['get']

    def get(self, request, *args):
        # print(request.user.is_anonymous)
        if not request.user.is_anonymous:
            logout(request)
            return Response('Logout successfully', status.HTTP_200_OK)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Not login yet'
            }, status.HTTP_400_BAD_REQUEST)


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


class TryonViewSet(APIView):
    def get(self, request, *args):
        print(request.query_params)
        customer_image_dir = os.path.join(settings.MEDIA_ROOT, "customers", "customer_" + request.query_params.get("customer_name"))
        customer_image_path = os.path.join(customer_image_dir, os.listdir(customer_image_dir)[0])

        product_image_dir = os.path.join(settings.MEDIA_ROOT, "products", request.query_params.get("customer_name"))
        product_image_path = os.path.join(product_image_dir, os.listdir(product_image_dir)[0])

        # import os

        # os_dir = os.getcwd()
        # os.chdir(os.path.join(os_dir, "model"))
        # test = "python test.py --name deepfashion --dataset_mode deepfashion --dataroot ../media --gpu_ids 0 --nThreads 0 --batchSize 1 --use_attention --PONO --PONO_C --save_per_img --warp_bilinear --no_flip --warp_patch --video_like --adaptor_kernel 4"
        # image = os.system(test)
        # os.chdir(os_dir)
        
        image = tryon()

        # path = "/media/tryon/{}_{}.jpg".format(request.query_params.get('customer_name'), request.query_params.get('product_id'))
        # image.save(path)

        data = [{"url": path}]
        serializer = TryonSerializer(data, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
