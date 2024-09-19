from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf.urls.static import static
from quartel import settings
=======
from django.contrib.auth import views as auth_views
>>>>>>> 56be9eb (Primeiro commit: adicionando todos os arquivos do projeto)
=======
from django.conf.urls.static import static
from quartel import settings
>>>>>>> 5d62f37 (User Registration funcionando)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('arranchamento.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de login/logout

]

if settings.DEBUG:
<<<<<<< HEAD
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> 56be9eb (Primeiro commit: adicionando todos os arquivos do projeto)
=======
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 5d62f37 (User Registration funcionando)
