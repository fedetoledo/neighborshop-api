from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import DetailView
from api.models import Product, ProductImage, Market
from ..forms import ProductImageForm, ProductCreateForm, ProductUpdateForm

class ProductCreateView(CreateView):
    template_name = "products/create.html"
    form_class = ProductCreateForm
    success_url = reverse_lazy('market')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imageForm"] = ProductImageForm(self.request.POST, self.request.FILES)
        return context

    def form_valid(self, form):
        market = Market.objects.get(owner__id=self.request.user.id)
        form.instance.market = market
        form.instance.save()
        images = self.request.FILES.getlist('image')
        for image in images:
            product_image = ProductImage(image=image, product=form.instance)
            product_image.save()
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/edit.html"
    form_class = ProductUpdateForm

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.kwargs['pk']})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('market')

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductImage.objects.filter(product=context['product'])
        return context
        