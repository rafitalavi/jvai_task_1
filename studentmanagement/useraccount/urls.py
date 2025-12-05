from django.urls import path , include
from .views import UserRegistrationViewset , LoginViewset

urlpatterns = [
    path('register/', UserRegistrationViewset.as_view(), name='user-register'),
    path('login/', LoginViewset.as_view(), name='user-login'),
]