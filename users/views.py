<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  
    success_url = reverse_lazy('index')

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
=======
>>>>>>> 5d62f37 (User Registration funcionando)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomLoginView(LoginView):
<<<<<<< HEAD
    template_name = 'users/login.html'  # O template para a página de login
    redirect_authenticated_user = True  # Redirecionar se o usuário já estiver logado
<<<<<<< HEAD
    success_url = reverse_lazy('home') 
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
=======
    success_url = reverse_lazy('index') 
>>>>>>> d7522b7 (Correcao Login/Logout e estética visual)
=======
    template_name = 'users/login.html'
    redirect_authenticated_user = True  
    success_url = reverse_lazy('index')

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
>>>>>>> 5d62f37 (User Registration funcionando)
