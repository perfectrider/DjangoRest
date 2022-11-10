from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'car_model', 'car_color', 'count')


admin.site.register(Order, OrderAdmin)
admin.site.register(CarModel)
admin.site.register(CarBrand)
admin.site.register(CarColor)
