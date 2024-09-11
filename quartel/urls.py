from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('arranchamento.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de login/logout

]
