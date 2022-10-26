import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class OrderModel:
#     def __init__(self, order_date, car_model, car_color, count):
#         self.order_date = order_date
#         self.car_model = car_model
#         self.car_color = car_color
#         self.count = count


class OrderSerializer(serializers.Serializer):

    order_date = serializers.DateField()
    car_model = serializers.CharField()
    car_brand = serializers.CharField()
    car_color = serializers.CharField()
    count = serializers.IntegerField()


    def create(self, validated_data):
        return Order.objects.create(**validated_data)

# def encode():
#     model = OrderModel('order_date: 2022-10-18',
#                        'car_model: volkswagen',
#                        'car_color: 1',
#                        'count: 3')
#     model_sr = OrderSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
# #
# #
# def decode():
#     stream = io.BytesIO(b'{"order_date":"order_date: 2022-10-18","car_model":"car_model: volkswagen"}')
#     data = JSONParser().parse(stream)
#     serializer = OrderSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
