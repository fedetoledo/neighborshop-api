from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView

from api.models import Product, ProductImage, Market
from ..forms import ProductImageForm, NewProductForm
from ..utils import save_product_image_to_database

def createProductView(request):

	if request.method == 'POST':
		new_product_form = NewProductForm(request.POST)
		product_images_form = ProductImageForm(request.POST, request.FILES)
		product_images = request.FILES.getlist('image')
		if new_product_form.is_valid() and product_images_form.is_valid():
			new_product = new_product_form.save(commit=False)
			new_product.market = Market.objects.get(owner__id=request.user.id)
			new_product.save()
			for image in product_images:
				product_image = ProductImage(image=image, product=new_product)
				product_image.save()
				
			return redirect('detalle', pk=new_product.id)
	else:
		new_product_form = NewProductForm()
		product_images_form = ProductImageForm()
		return render(request, 'products/create-product.html',{'productForm':new_product_form,'imageForm':product_images_form})

class ProductUpdateView(UpdateView):
	model = Product
	template_name = "products/edit-product.html"
	fields = '__all__'

	def get_success_url(self):
	    return reverse_lazy('detalle', kwargs={'pk': self.kwargs['pk']})

class ProductDeleteView(DeleteView):
	model = Product
	template_name = 'products/confirm-delete.html'
	success_url = reverse_lazy('tienda')

class ProductDetailView(DetailView):
	model = Product
	context_object_name = "product"
	template_name = "products/details.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['images'] = ProductImage.objects.filter(product=context['product'])
		return context
		