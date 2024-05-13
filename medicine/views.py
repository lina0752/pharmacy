from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Medicine


class MListView(ListView):
    model = Medicine
    template_name = 'medicine/list.html'
    context_object_name = 'medicine'


class MDetailView(DetailView):
    model = Medicine
    template_name = 'medicine/detail.html'
    context_object_name = 'medicine'


class MCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    fields = ['title', 'description', 'image']
    template_name = 'medicine/create.html'
    success_url = reverse_lazy('medicine:list')

    def form_valid(self, form):
        form.instance.submitter = self.request.user

        return super().form_valid(form)


class UserIsSubmitter(UserPassesTestMixin):
    # Custom method
    def get_photo(self):
        return get_object_or_404(Medicine, pk=self.kwargs.get('pk'))

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(submitter=self.request.user)


# class PhotoUpdateView(UserPassesTestMixin, UpdateView):
class MUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    template_name = 'medicine/update.html'
    model = Medicine
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('medicine:list')


class MDeleteView(PermissionRequiredMixin, DeleteView ):
    # specify the model you want to use
    model = Medicine
    success_url = reverse_lazy('medicine:list')
    template_name = 'medicine/delete.html'
    permission_required = 'medicine.can_delete'