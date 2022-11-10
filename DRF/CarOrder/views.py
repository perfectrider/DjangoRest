from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


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

