from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Certifique-se de que o CustomUser foi transferido corretamente

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['idt_mil', 'posto', 'nome', 'nome_guerra', 'subunidade']
