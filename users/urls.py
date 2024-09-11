from django.urls import path
<<<<<<< HEAD
from .views import CustomLoginView, UserRegisterView
=======
from . import views
from .views import CustomLoginView
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
<<<<<<< HEAD
    path('register/', UserRegisterView.as_view(), name='register'),

=======
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
]