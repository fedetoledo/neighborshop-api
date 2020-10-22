from django import forms
from api.models import Product, ProductImage, User, Market

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

class ProductCreateForm(forms.ModelForm):
    categories = forms.MultipleChoiceField(
        label='Categorias',
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'categories-checkbox',
        }),
        choices=CATEGORIES_CHOICES
    )
    class Meta:
        model = Product
        fields = ['name','description','price','categories']
        labels = {
            'name': 'Nombre del producto',
            'description': 'Descripcion del producto',
            'price': 'Precio del producto',
        }
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

class ProductUpdateForm(forms.ModelForm):
    categories = forms.MultipleChoiceField(
        label='Categorias',
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'categories-checkbox',
        }),
        choices=CATEGORIES_CHOICES
    )
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'categories']
        labels = {
            'name': 'Nombre del producto',
            'description': 'Descripcion del producto',
            'price': 'Precio del producto',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Nombre del producto',
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Descripcion del producto',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'input',
                'placeholder': 'Precio del producto',
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

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
            'email', 'password', 'phone_number', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Apellido'
            }),
            'username': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Nombre de usuario'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Email'
            }),
            'password': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Contraseña',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Numero de telefono'
            }),
        }

class CreateMarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['name', 'description', 'logo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Nombre de tu tienda',
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Contale a tu clientes quien sos'
            }),
        }

class UpdateMarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['name', 'description', 'logo', 'phone_number']
        labels = {
            'name': 'Nombre de la tienda',
            'description': 'Descripcion de la tienda',
            'phone_number': 'Numero de telefono'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
            })
        }
