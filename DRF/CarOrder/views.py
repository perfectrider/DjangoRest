from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


# class OrderAPIView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderAPIView(APIView):
    def get(self, request):
        o = Order.objects.all()
        return Response({'orders': OrderSerializer(o, many=True).data})

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'order': serializer.data})
