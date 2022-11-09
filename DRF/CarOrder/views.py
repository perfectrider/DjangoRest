from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderAPIView(APIView):
    def get(self, request):
        o = Order.objects.all()
        return Response({'orders': OrderSerializer(o, many=True).data})

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Order.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = OrderSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)