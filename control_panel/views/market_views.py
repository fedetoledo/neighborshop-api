from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from ..forms import CreateMarketForm
from api.models import Market

class MarketCreateView(CreateView):
    form_class = CreateMarketForm
    template_name = "market/create.html"
    success_url = reverse_lazy('tienda')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MarketDeleteView(DeleteView):
    model = Market
    template_name = 'market/confirm-delete.html'
    success_url = reverse_lazy('tienda')

class MarketDetailView(DetailView):
    model = Market
    template_name = "market/detail.html"
