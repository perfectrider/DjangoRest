from django.db import models


class Order(models.Model):
    '''Класс заказов'''

    order_date = models.DateField(blank=True, null=True, verbose_name='Дата заказа')
    car_model = models.ForeignKey('CarModel', blank=False, on_delete=models.PROTECT, verbose_name='Модель авто')
    car_color = models.ForeignKey('CarColor', blank=False, on_delete=models.PROTECT, verbose_name='Цвет авто')
    count = models.IntegerField(blank=False, verbose_name='Количество авто')

    def __str__(self):
        return f"{str(self.order_date)} - {self.car_model}, кол-во: {self.count}"


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']


class CarModel(models.Model):
    '''Класс моделей авто'''

    model_of_car = models.CharField(blank=False, max_length=50, verbose_name='Модель авто')
    brand_of_car = models.ForeignKey('CarBrand',
                                     on_delete=models.PROTECT,
                                     blank=False,
                                     verbose_name='Марка авто')

    def __str__(self):
        return self.model_of_car

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модели авто'


class CarBrand(models.Model):
    '''Класс марок авто'''

    brand = models.CharField(blank=False, max_length=50, verbose_name='Марка авто')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марки авто'

class CarColor(models.Model):
    '''Класс цвета авто'''

    color = models.CharField(blank=False, max_length=50, verbose_name='Цвет авто')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет авто'
        verbose_name_plural = 'Цвета авто'
