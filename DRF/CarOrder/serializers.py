from rest_framework import serializers
from .models import *
from datetime import date


class BrandField(serializers.ModelSerializer):
    brand_of_car = serializers.SlugRelatedField(slug_field='brand',
                                                queryset=CarBrand.objects)

    class Meta:
        model = CarModel
        fields = ['brand_of_car']


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField(default=date.today, label='Дата заказа')

    car_model = serializers.SlugRelatedField(slug_field='model_of_car',
                                             queryset=CarModel.objects,
                                             label='Модель авто')

    brands = BrandField(many=True, read_only=True)

    car_color = serializers.SlugRelatedField(slug_field='color',
                                             queryset=CarColor.objects,
                                             label='Цвет авто')

    class Meta:
        model = Order
        fields = ['order_date', 'car_model', 'brands', 'car_color', 'count']

    # Если используется "serializer.Serializer":

    # order_date = serializers.DateField()
    # car_model = serializers.SlugRelatedField(slug_field='model_of_car', queryset=CarModel.objects)
    # car_color = serializers.SlugRelatedField(slug_field='color', queryset=CarColor.objects)
    # count = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Order.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.order_date = validated_data.get('order_date', instance.order_date)
    #     instance.car_model = validated_data.get('car_model', instance.car_model)
    #     instance.car_color = validated_data.get('car_color', instance.car_color)
    #     instance.count = validated_data.get('count', instance.count)
    #     instance.save()
    #     return instance
    #
    # def delete(self, validated_data):
    #     return Order.objects.delete(**validated_data)
