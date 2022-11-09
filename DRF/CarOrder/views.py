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

