from django.urls import path
from . import views
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('arranchamento/', views.arranchar_usuario, name='arranchar_usuario'),
    path('listar_refeicoes/', views.listar_refeicoes, name='listar_refeicoes'),
    path('excluir_arranchamento/<int:arranchamento_id>/', views.excluir_arranchamento, name='excluir_arranchamento'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('arranchamentos_dia/', views.verificar_arranchamentos, name='verificar_arranchamentos'),

=======
=======
from django.contrib.auth import views as auth_views

>>>>>>> d7522b7 (Correcao Login/Logout e estética visual)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('arranchamento/', views.arranchar_usuario, name='arranchar_usuario'),
    path('listar_refeicoes/', views.listar_refeicoes, name='listar_refeicoes'),
<<<<<<< HEAD
>>>>>>> 56be9eb (Primeiro commit: adicionando todos os arquivos do projeto)
=======
    path('excluir_arranchamento/<int:arranchamento_id>/', views.excluir_arranchamento, name='excluir_arranchamento'),
<<<<<<< HEAD
>>>>>>> fa0a5d4 (View listar_refeicoes funcionando com a funcionalidade cancelar refeicoes)
=======
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

>>>>>>> d7522b7 (Correcao Login/Logout e estética visual)
]