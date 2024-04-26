from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
# from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import StockItem

class StockItemList(LoginRequiredMixin, ListView):
    model = StockItem
    template_name = 'medicine/list.html'
    context_object_name = 'stock_items'

class StockItemDetail(LoginRequiredMixin, DetailView):
    model = StockItem
    template_name = 'medicine/detail.html'
    context_object_name = 'stock_item'

class StockItemCreate(LoginRequiredMixin, CreateView):
    model = StockItem
    fields = ['medicine', 'quantity', 'price', 'expiration_date']
    template_name = 'medicine/create.html'
    success_url = reverse_lazy('medicine:list')

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)

class StockItemUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StockItem
    fields = ['medicine', 'quantity', 'price', 'expiration_date']
    template_name = 'medicine/update.html'
    success_url = reverse_lazy('medicine:list')

    def test_func(self):
        stock_item = self.get_object()
        return self.request.user == stock_item.submitter

class StockItemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = StockItem
    template_name = 'medicine/delete.html'
    success_url = reverse_lazy('medicine:list')

    def test_func(self):
        stock_item = self.get_object()
        return self.request.user == stock_item.submitter

# class SaleList(LoginRequiredMixin, ListView):
#     model = Sale
#     template_name = 'medicine/sale_list.html'
#     context_object_name = 'sales'
#
# class SaleDetail(LoginRequiredMixin, DetailView):
#     model = Sale
#     template_name = 'medicine/sale_detail.html'
#     context_object_name = 'sale'
#
# class SaleCreate(LoginRequiredMixin, CreateView):
#     model = Sale
#     fields = ['stock_item', 'quantity_sold', 'total_price']
#     template_name = 'medicine/sale_create.html'
#     success_url = reverse_lazy('medicine:sale_list')
#
#     def form_valid(self, form):
#         form.instance.sold_by = self.request.users
#         return super().form_valid(form)
#
# class SaleUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Sale
#     fields = ['stock_item', 'quantity_sold', 'total_price']
#     template_name = 'medicine/sale_update.html'
#     success_url = reverse_lazy('medicine:sale_list')
#
#     def test_func(self):
#         sale = self.get_object()
#         return self.request.users == sale.sold_by
#
# class SaleDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Sale
#     template_name = 'medicine/sale_delete.html'
#     success_url = reverse_lazy('medicine:sale_list')
#
#     def test_func(self):
#         sale = self.get_object()
#         return self.request.users == sale.sold_by
