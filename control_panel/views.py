from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import DetailView, ListView
from django.views import View
from api.models import Product, ProductImage, User, Market
from .forms import UserLoginForm, NewProductForm, ProductImageForm, CreateUserForm
from google.cloud import storage
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import uuid
import pathlib
from google.cloud.storage.blob import Blob
from django.urls import reverse_lazy
from firebase import firebase

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
			product_instance.market = Market.objects.get(owner__uid=request.session['user']['localId'])
			# product_instance.businessId = 21 #User business id
			product_instance.save()
			for f in files:
				f.name = get_random_name(f.name)
				file_instance = ProductImage(image=f, product=product_instance)
				file_instance.save()

				#Upload image to remote bucket
				file_path = str(pathlib.Path().absolute())+ "/media/temp/" + f.name
				businessFolder = "businesses/"+str(product_instance.market)+"/"+f.name
				upload_blob(file_path, businessFolder)

				#Download url and save to db
				current_image = ProductImage.objects.get(image=file_instance.image)
				current_image.remoteURL = "https://storage.googleapis.com/barrio-ecommerce.appspot.com/businesses/"+str(product_instance.market)+"/"+f.name
				current_image.save()
				
			return redirect('detalle', pk=product_instance.id)
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

	if request.session['user']:
		return render(request, 'user/profile.html')
	return render(request, 'home.html')

def loginFirebase(email, password):
	firebase = firebase.FirebaseApplication('https://')

class UserLoginView(FormView):
	form_class = UserLoginForm
	template_name = 'auth/login.html'
	success_url = reverse_lazy('productos:profile')

	def form_valid(self, form):
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']

		auth = firebase.auth()

		user = auth.sign_in_with_email_and_password(email, password)

		self.request.session['user'] = user
		return super().form_valid(form)

class CreateUserView(CreateView):
	form_class = CreateUserForm
	template_name = 'auth/signup.html'
	success_url = reverse_lazy('productos:home')

	def form_valid(self, form):
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']

		auth = firebase.auth()

		signup = auth.create_user_with_email_and_password(email, password)

		print('signup: ', signup)

		return super().form_valid(form)

def profileView(request):
	uid = request.session['user']['localId']

	user = User.objects.get(uid=uid)
	products = Product.objects.filter(market__owner__uid=uid)

	return render(request, 'user/profile.html', {'products': products, 'user': user})