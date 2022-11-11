from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, CarColor, CarBrand
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    # Можно убрать, если при регистрации роутера указать атрибут 'basename='order'
    serializer_class = OrderSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Order.objects.all()

        return Order.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    # Если detail=True, то будет возвращаться не список записей, а одна

    def by_colors(self, request):
        # !ВЫВОД заказов по цветам. (атрибуты: цвет, количество)
        colors = CarColor.objects.all()
        return Response({'Colors': [c.color for c in colors]})

    @action(methods=['get'], detail=False)
    def by_brands(self, request):
        # !ВЫВОД заказов по брендам. (атрибуты: бренд, количество)
        brands = CarBrand.objects.all()
        return Response({'Brands': [c.brand for c in brands]})



# ----------------------------------------------------
#  Классы Generics (При работе с большими проектами их использовать неоптимально,
# т.к. будет много повторяющегося кода в каждом из классов)

# class OrderAPIList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderAPIUpdate(generics.UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# ---------------------------------------------------
# Класс для использование с serializes.Serializers:

# class OrderAPIView(APIView):
#     def get(self, request):
#         o = Order.objects.all()
#         return Response({'orders': OrderSerializer(o, many=True).data})
#
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Order.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = OrderSerializer(data=request.data, instance=instance)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             instance = Order.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = OrderSerializer(data=request.data, instance=instance)
#         if serializer.is_valid():
#             serializer.delete()
#
#         return Response({'order': 'order deleted ' + str(pk)})

