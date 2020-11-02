# from django.urls import include, path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from BackendManagement.views import *

routers = routers.DefaultRouter()
routers.register('salers', SalerViewSet)
routers.register('customers', CustomerViewSet)


urlpatterns = [
    url('', include(routers.urls)),
    url('saler/signup', SalerSignupViewSet.as_view({'post': 'create'})),
    url('customer/signup', CustomerSignupViewSet.as_view({'post': 'create'}))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)