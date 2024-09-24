from django.contrib import admin
from .models import CustomUser, Refeicao, Arranchamento

# Registra os modelos na página de administração
admin.site.register(CustomUser)
admin.site.register(Refeicao)
admin.site.register(Arranchamento)
