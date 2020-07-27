from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.signals import request_finished

from firebase import firebase

from api.models import User, Product, Market
from ..forms import UserLoginForm, UserCreateForm
from ..utils import signup_and_login_from_firebase, get_current_user

class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('tienda')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        auth = firebase.auth()

        user = auth.sign_in_with_email_and_password(email, password)

        self.request.session['user'] = user
        
        return super().form_valid(form)
    
class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('nueva-tienda')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        pre_save.connect(handle_new_user, sender=User, dispatch_uid='new_user_signal')
        return super().form_valid(form)

@receiver(pre_save, sender=User, dispatch_uid='new_user_signal')
def handle_new_user(sender, **kwargs):
    new_user = kwargs.get('instance')
    email = new_user.email
    password = new_user.password

    user_uid = signup_and_login_from_firebase(email, password)

    new_user.uid = user_uid


def profileView(request):
    if 'user' in request.session:
        user = get_current_user(request)
        products = Product.objects.filter(market__owner__uid=user.uid)
        market = Market.objects.get(owner__uid=user.uid)
        return render(request, 'user/profile.html', {'market': market, 'products': products, 'user': user})
    return render(request, 'auth/login.html')

def logoutView(request):
    #Delete the session id cookie
    # del request.session['user']
    logout(request)
    return redirect('tienda/login')