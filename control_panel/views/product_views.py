from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView

from api.models import Product, ProductImage, Market
from ..forms import ProductImageForm, NewProductForm
from ..utils import save_product_image_to_remote

def createProductView(request):

	if request.method == 'POST':
		form = NewProductForm(request.POST)
		image_form = ProductImageForm(request.POST, request.FILES)
		files = request.FILES.getlist('image')
		if form.is_valid() and image_form.is_valid():
			product_instance = form.save(commit=False)
			product_instance.market = Market.objects.get(owner__uid=request.session['user']['localId'])
			# product_instance.businessId = 21 #User business id
			product_instance.save()
			for image in files:
				save_product_image_to_remote(image, product_instance)
				# f.name = get_random_name(f.name)
				# file_instance = ProductImage(image=f, product=product_instance)
				# file_instance.save()

				# #Upload image to remote bucket
				# file_path = str(pathlib.Path().absolute())+ "/media/temp/" + f.name
				# marketsFolder = "markets/"+str(product_instance.market)+"/"+f.name
				# upload_image_gcs(file_path, marketsFolder)

				# #Download url and save to db
				# current_image = ProductImage.objects.get(image=file_instance.image)
				# current_image.remoteURL = "https://storage.googleapis.com/barrio-ecommerce.appspot.com/businesses/"+str(product_instance.market)+"/"+f.name
				# current_image.save()
				
			return redirect('detalle', pk=product_instance.id)
		else:
			return redirect('home')
	else:
		form = NewProductForm()
		image_form = ProductImageForm()
		return render(request, 'products/create-product.html',{'productForm':form,'imageForm':image_form})

class ProductUpdateView(UpdateView):
	model = Product
	template_name = "products/edit-product.html"
	fields = '__all__'
	success_url = '../'

class ProductDeleteView(DeleteView):
	model = Product
	template_name = 'products/confirm-delete.html'
	success_url = reverse_lazy('tienda')

class ProductDetailView(DetailView):
	model = Product
	template_name = "products/details.html"
