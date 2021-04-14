from .views import order_create, order_delete

from django.urls import path

urlpatterns = [
    path('order/create', order_create, name='shopify_order_create'),
    path('order/delete', order_delete, name='shopify_order_delete'),
]
