from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from api.models import User, Product, Market
from ..forms import UserLoginForm, UserCreateForm
from ..utils import signup_and_login_from_firebase

class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('tienda')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print('USER ACTIVE, TRYING TO LOGIN')
            login(self.request, user)
        return super().form_valid(form)
    
class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('nueva-tienda')

    def form_valid(self, form):
        user_data = form.save(commit=False)

        username = user_data.username
        password = user_data.password

        user_data.password = make_password(password)
        user_data.save()
        # TODO handle user signup error
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)

@login_required
def profileView(request):
    user = request.user
    products = Product.objects.filter(market__owner__uid=user.uid)
    market = Market.objects.get(owner__uid=user.uid)
    return render(request, 'user/profile.html', {'products': products, 'user': user})

@login_required
def logoutView(request):
    #Delete the session id cookie
    # del request.session['user']
    logout(request)
    return redirect('tienda/login')