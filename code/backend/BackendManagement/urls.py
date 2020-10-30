# from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from BackendManagement.views import SalerViewSet, SalerSignupViewSet

routers = routers.DefaultRouter()
routers.register('salers', SalerViewSet)


urlpatterns = [
    url('', include(routers.urls)),
    url('saler/signup', SalerSignupViewSet.as_view({'post': 'create'}))
]
