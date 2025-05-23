from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from quartel import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('arranchamento.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de login/logout

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
