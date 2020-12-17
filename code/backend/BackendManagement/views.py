import os
import shutil

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.conf import settings
from django.utils import timezone

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_haystack.viewsets import HaystackViewSet

from fluent_comments.models import FluentComment
from django.contrib.contenttypes.models import ContentType

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
            pics_path = os.path.join(settings.MEDIA_ROOT, 'customers', 'customer_' + str(customer), 'img')
            tryon_path = os.path.join(settings.MEDIA_ROOT, 'customers', 'customer_' + str(customer), 'tryon')
            pose_path = os.path.join(settings.MEDIA_ROOT, 'customers', 'customer_' + str(customer), 'pose')
            previous_pics = os.listdir(pics_path)
            for previous_pic in previous_pics:
                if os.path.join('customers', 'customer_' + str(customer), 'img', previous_pic) != data['self_pics']:
                    os.remove(os.path.join(pics_path, previous_pic))
            if os.path.exists(tryon_path):
                previous_tryon = os.listdir(tryon_path)
                for p in previous_tryon:
                    os.remove(os.path.join(tryon_path, p))
            if os.path.exists(pose_path):
                previous_pose = os.listdir(pose_path)
                for p in previous_pose:
                    os.remove(os.path.join(pose_path, p))
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

    def list(self, request):
        if len(request.query_params) == 0:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            try:
                queryset = Product.objects.filter(owned_saler=request.query_params['owned_saler'])
                serializer = ProductSerializer(queryset, many=True)
            except Exception as e:
                return Response({
                    'status': 'Bad request',
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data)

    def partial_update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        data = request.data.copy()
        
        if data.get('pics'):
            pics_path = os.path.join(settings.MEDIA_ROOT, 'products', str(product.id), 'img')
            pose_path = os.path.join(settings.MEDIA_ROOT, 'products', str(product.id), 'pose')
            if os.path.exists(pose_path):
                for pose in os.listdir(pose_path):
                    os.remove(os.path.join(pose_path, pose))
            for previous_pic in os.listdir(pics_path):
                if os.path.join('products', str(product.id), 'img', previous_pic) != data['pics']:
                    os.remove(os.path.join(pics_path, previous_pic))
            customers_path = os.path.join(settings.MEDIA_ROOT, 'customers')
            if os.path.exists(customers_path):
                for customer in os.listdir(customers_path):
                    tryon_result = os.path.join(customers_path, customer, 'tryon', '{}_{}.jpg'.format(customer[len("customer_"):], str(product.id)))
                    if os.path.exists(tryon_result):
                        os.remove(tryon_result)
        
        serializer = ProductSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', 'message': "Update the product's info successfully"}, status.HTTP_200_OK)
        return Response({'status': 'Internal Error', 'message': "Failed to update product information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        customer_image_pose = os.path.join(settings.MEDIA_ROOT, "customers", "customer_" + request.query_params.get("customer_name"), "pose")
        product_image_pose = os.path.join(settings.MEDIA_ROOT, "products", request.query_params.get("product_name"), "pose")
        if not os.path.exists(customer_image_pose):
            os.makedirs(customer_image_pose)
        if not os.path.exists(product_image_pose):
            os.makedirs(product_image_pose)

        customer_image_dir = os.path.join(settings.MEDIA_ROOT, "customers", "customer_" + request.query_params.get("customer_name"), "img")

        product_image_dir = os.path.join(settings.MEDIA_ROOT, "products", request.query_params.get("product_name"), "img")

        customer_name = "customer_" + request.query_params.get("customer_name")
        customer_image_id = os.listdir(customer_image_dir)[0]
        product_name = "" + request.query_params.get("product_name")
        product_image_id = os.listdir(product_image_dir)[0]
        
        print(request.query_params)
        path = "/media/customers/customer_{}/tryon/{}_{}.jpg".format(request.query_params.get("customer_name"), request.query_params.get("customer_name"), product_name)
        tryon_dir = os.path.join(settings.MEDIA_ROOT, "customers", "customer_{}".format(request.query_params.get("customer_name")), "tryon")
        data = [{"url": path}]
        serializer = TryonSerializer(data, many=True).data
        
        if os.path.exists(os.path.join(tryon_dir, "{}_{}.jpg".format(request.query_params.get("customer_name"), request.query_params.get("product_name")))):
            return Response(serializer, status=status.HTTP_200_OK)
        print("Start")
        image = tryon(customer_image_id, product_image_id, customer_name, product_name)
        print("Finish")

        if not os.path.exists(tryon_dir):
            os.mkdir(tryon_dir)
        image.save(os.path.join(tryon_dir, "{}_{}.jpg".format(request.query_params.get("customer_name"), product_name)))

        return Response(serializer, status=status.HTTP_200_OK)


class ProductSearchViewset(HaystackViewSet):
    index_models = [Product]
    serializer_class = ProductSearchSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = FluentComment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = self.request.data
            comment = data['comment']
            product = data['product']
            if 'parent' in data:
                parent = data['parent']
            else:
                parent = None
            submit_date = timezone.now()
            content = ContentType.objects.get(app_label="BackendManagement", model="product").pk
            comment = FluentComment.objects.create(object_pk=product, comment=comment, submit_date=submit_date,
                                                   content_type_id=content, user_id=self.request.user.name, site_id=settings.SITE_ID, parent_id=parent)
            serializer = CommentSerializer(
                comment, context={'request': request})
            return Response(serializer.data)
        return Response({
            'status': 'Bad request',
            'message': 'Not login yet'
        }, status.HTTP_400_BAD_REQUEST)
