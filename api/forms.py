from django import forms
from .models import Product, ProductImage, User

CATEGORIES_CHOICES = [
	('Comidas', 'Comidas'),
	('Postres', 'Postres'),
	('Decoración', 'Decoración'),
	('Regalos', 'Regalos'),
	('Servicios', 'Servicios'),
	('Profesionales', 'Profesionales'),
	('Jardinería', 'Jardinería'),
	('Educación', 'Educación'),
	('Belleza y Salud', 'Belleza y Salud'),
	('Usados', 'Usados'),
	('Bebidas', 'Bebidas'),
]

class NewProductForm(forms.ModelForm):
	categories = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple(attrs={
			'class': 'categories-checkbox',
		}),
		choices=CATEGORIES_CHOICES
	)
	class Meta:
		model = Product
		fields = ['name','description','price','categories']
		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'input',
				'placeholder': 'Nombre del producto'
				}),
			'description': forms.Textarea(attrs={
				'class': 'textarea',
				'placeholder': 'Descripcion'
				}),
			'price': forms.NumberInput(attrs={
				'class': 'input',
				'placeholder': 'Precio'
				}),
		}

class ProductImageForm(forms.ModelForm):
	class Meta:
		model = ProductImage
		fields = ['image']
		widgets= {
			'class': 'button is-primary',
			'image': forms.ClearableFileInput(attrs={'multiple': True}),
		}

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email','password']

class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ['uid', 'userPicture']