from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.Serializer):
    order_date = serializers.DateField()
    car_model = serializers.SlugRelatedField(slug_field='model_of_car', queryset=CarModel.objects)
    car_color = serializers.SlugRelatedField(slug_field='color', queryset=CarColor.objects)
    count = serializers.IntegerField()

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

