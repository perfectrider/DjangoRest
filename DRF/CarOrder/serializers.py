import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField()
    car_model = serializers.SlugRelatedField(slug_field='model_of_car', queryset=CarModel.objects)
    car_color = serializers.SlugRelatedField(slug_field='color', queryset=CarColor.objects)
    count = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('order_date', 'car_model', 'car_color', 'count')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

