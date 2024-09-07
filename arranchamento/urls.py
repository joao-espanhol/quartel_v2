from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register_view, name='register'),
    path('arranchamento/', views.arranchar_usuario, name='arranchar_usuario'),
    path('listar_refeicoes/', views.listar_refeicoes, name='listar_refeicoes'),
]