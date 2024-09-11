from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # O template para a página de login
    redirect_authenticated_user = True  # Redirecionar se o usuário já estiver logado
    success_url = reverse_lazy('home') 