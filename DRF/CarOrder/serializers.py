from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.Serializer):
    order_date = serializers.DateField()
    car_model = serializers.SlugRelatedField(slug_field='model_of_car', queryset=CarModel.objects)
    car_color = serializers.SlugRelatedField(slug_field='color', queryset=CarColor.objects)
    count = serializers.IntegerField()

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.car_model = validated_data.get('car_model', instance.car_model)
        instance.car_color = validated_data.get('car_color', instance.car_color)
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        return instance