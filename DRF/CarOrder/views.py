from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import *


# class OrderAPIView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Orders'})