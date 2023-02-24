from django.urls import path

from .views import item_detail, buy_item, success_view, cancel_view

urlpatterns = [
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('buy-item/<int:item_id>/', buy_item, name='buy-item'),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
]
