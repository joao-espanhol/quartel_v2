from django.urls import path
from .views import CustomLoginView, UserRegisterView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),

]