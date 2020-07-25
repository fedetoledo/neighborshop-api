from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


from ..forms import CreateMarketForm
from api.models import Market

def MarketCreateView(request):

    if request.method == 'POST':
        form = CreateMarketForm(request.POST)
        if form.is_valid():
            market_instance = form.save(commit=False)
            
            #Set current user as owner, pass uid
            uid = request.session['uid']['localId']
            userID = User.objects.get(uid=uid)
            market_instance.owner = userID
            market_instance.save()

            return redirect('tienda')
        else:
            return
    else:
        form = CreateMarketForm()
        return render(request, 'market/create.html', {'form': form})

class MarketDeleteView(DeleteView):
    model = Market
    template_name = 'market/confirm-delete.html'
    success_url = reverse_lazy('tienda')

class MarketDetailView(DetailView):
    model = Market
    template_name = "market/detail.html"
