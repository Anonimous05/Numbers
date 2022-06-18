from django.urls import path
from orders.api import OrdersListAPIView

urlpatterns = [
    path('', OrdersListAPIView.as_view())
]
