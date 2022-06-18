from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order
from orders.serializers.view import OrderSerializer


class OrdersListAPIView(APIView):
    serializer_class = OrderSerializer

    def get(self, request):
        serialized_data = self.serializer_class(Order.objects.all(), many=True).data
        return Response(data=serialized_data, status=status.HTTP_200_OK)
