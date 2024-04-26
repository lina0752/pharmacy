'''Photoapp URL patterns'''
from django.views.generic import TemplateView
from django.urls import path

from medicine.views import StockItemList, StockItemDetail, StockItemCreate, StockItemUpdate, StockItemDelete

app_name = 'photo'

urlpatterns = [
    path('', StockItemList.as_view(), name='list'),
    path('photo/<int:pk>/', StockItemDetail.as_view(), name='detail'),
    path('photo/create/', StockItemCreate.as_view(), name='create'),
    path('photo/<int:pk>/update/', StockItemUpdate.as_view(), name='update'),
    path('photo/<int:pk>/delete/', StockItemDelete.as_view(), name='delete'),
]

