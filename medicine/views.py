from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Medicine


class MedListView(ListView):
    model = Medicine
    template_name = 'medicine/list.html'
    context_object_name = 'medicine'

class MedDetailView(DetailView):
    model = Medicine
    template_name = 'medicine/detail.html'
    context_object_name = 'medicine'