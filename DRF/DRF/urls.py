"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CarOrder.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/order/

    # path('api/v1/orderlist/', OrderViewSet.as_view({'get': 'list'})),
    # path('api/v1/orderlist/<int:pk>', OrderViewSet.as_view({'put': 'update'}))
    # URL для использования с классом представлений ViewSet, без использования routers

    # path('api/v1/orderlist/', OrderAPIList.as_view()),
    # path('api/v1/orderlist/<int:pk>/', OrderAPIUpdate.as_view()),
    # path('api/v1/orderdetail/<int:pk>/', OrderAPIDetailView.as_view())
#     URL для использования с классами представлений generics
]
