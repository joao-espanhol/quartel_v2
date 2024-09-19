from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import CustomLoginView, UserRegisterView
=======
from . import views
from .views import CustomLoginView
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
=======
from .views import CustomLoginView, UserRegisterView
>>>>>>> 5d62f37 (User Registration funcionando)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('register/', UserRegisterView.as_view(), name='register'),

=======
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
=======
    path('register/', UserRegisterView.as_view(), name='register'),

>>>>>>> 5d62f37 (User Registration funcionando)
]