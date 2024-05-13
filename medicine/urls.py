
from django.views.generic import TemplateView
from django.urls import path

from medicine.views import MListView, MDetailView, MCreateView, MUpdateView, MDeleteView

app_name = 'medicine'

urlpatterns = [
    path('', MListView.as_view(), name='list'),
    path('medicine/<int:pk>/', MDetailView.as_view(), name='detail'),
    path('medicine/create/', MCreateView.as_view(), name='create'),
    path('medicine/<int:pk>/update/', MUpdateView.as_view(), name='update'),
    path('medicine/<int:pk>/delete/', MDeleteView.as_view(), name='delete'),
]

