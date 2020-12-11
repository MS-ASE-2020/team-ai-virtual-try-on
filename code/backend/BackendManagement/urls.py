# from django.urls import include, path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from BackendManagement.views import *

routers = routers.DefaultRouter()
routers.register('salers', SalerViewSet)
routers.register('customers', CustomerViewSet)
routers.register('products', ProductViewSet)
routers.register('search', ProductSearchViewset, basename='product-search')
routers.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    url('', include(routers.urls)),
    url('saler/signup', SalerSignupViewSet.as_view({'post': 'create'})),
    url('customer/signup', CustomerSignupViewSet.as_view({'post': 'create'})),
    url('customer/login', CustomerLoginViewSet.as_view({'post': 'login'})),
    url('customer/logout', CustomerLogoutViewSet.as_view()),
    url('saler/login', SalerLoginViewSet.as_view({'post': 'login'})),
    url('saler/logout', SalerLogoutViewSet.as_view()),
    url('tryon', TryonViewSet.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
