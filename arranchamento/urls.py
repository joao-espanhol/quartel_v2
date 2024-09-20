from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('arranchamento/', views.arranchar_usuario, name='arranchar_usuario'),
    path('listar_refeicoes/', views.listar_refeicoes, name='listar_refeicoes'),
    path('excluir_arranchamento/<int:arranchamento_id>/', views.excluir_arranchamento, name='excluir_arranchamento'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('arranchamentos_dia/', views.verificar_arranchamentos, name='verificar_arranchamentos'),

]