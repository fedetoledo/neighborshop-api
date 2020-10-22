from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from api.models import Market
from ..forms import CreateMarketForm, UpdateMarketForm

class MarketCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateMarketForm
    template_name = "market/create.html"
    success_url = reverse_lazy('market')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MarketDeleteView(DeleteView):
    model = Market
    template_name = 'market/confirm-delete.html'
    success_url = reverse_lazy('market')

class MarketDetailView(DetailView):
    model = Market
    template_name = "market/detail.html"

class MarketUpdateView(UpdateView):
    form_class = UpdateMarketForm
    model = Market
    template_name = "market/edit.html"
    success_url = reverse_lazy('market')
    