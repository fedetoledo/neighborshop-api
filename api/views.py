from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Product, ProductImage
from .forms import NewProductForm, ProductImageForm
from google.cloud import storage
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import uuid
import pathlib
from google.cloud.storage.blob import Blob

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/federico/Escritorio/barrio-ecommerce/backend/ecommerce/credentials.json'

#GCS upload image to bucket
def upload_blob(source_file_name, destination_blob_name):
	bucket_name = "barrio-ecommerce.appspot.com"
	client = storage.Client()

	bucket = client.bucket(bucket_name)
	blob = bucket.blob(destination_blob_name)
	blob.upload_from_filename(source_file_name)
	blob.make_public()

#Random image name
def get_random_name(filename):
	ext = filename.split(".")[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	print(filename)
	return filename

# Create your views here.
def createProduct(request):

	if request.method == 'POST':
		form = NewProductForm(request.POST)
		image_form = ProductImageForm(request.POST, request.FILES)
		files = request.FILES.getlist('image')
		if form.is_valid() and image_form.is_valid():
			product_instance = form.save(commit=False)
			product_instance.businessId = 21 #User business id
			product_instance.save()
			for f in files:
				f.name = get_random_name(f.name)
				file_instance = ProductImage(image=f, product=product_instance)
				file_instance.save()

				#Upload image to remote bucket
				file_path = str(pathlib.Path().absolute())+ "/media/temp/" + f.name
				businessFolder = "businesses/"+str(product_instance.businessId)+"/"+f.name
				upload_blob(file_path, businessFolder)

				#Download url and save to db
				current_image = ProductImage.objects.get(image=file_instance.image)
				current_image.remoteURL = "https://storage.googleapis.com/barrio-ecommerce.appspot.com/businesses/"+str(product_instance.businessId)+"/"+f.name
				current_image.save()
				
			return redirect('details', pk=product_instance.id)
		else:
			return redirect('')
	else:
		form = NewProductForm()
		image_form = ProductImageForm()
		return render(request, 'products/create-product.html',{'productForm':form,'imageForm':image_form})

class ProductUpdateView(UpdateView):
	model = Product
	template_name = "products/edit-product.html"
	fields = '__all__'
	success_url = '../'

class ProductListView(ListView):
	model = Product
	template_name = "products/product-list.html"


class DetailProduct(DetailView):
	model = Product
	template_name = "products/details.html"

def HomeView(request):
	return render(request, 'home.html')