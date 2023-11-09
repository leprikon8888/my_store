from django.urls import path

from orders.views import OrderCreateView, SuccessTemplateView, CanceledTemplateView, OrderListView

from products.views import ProductsListView, basket_add, basket_remove

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
]


