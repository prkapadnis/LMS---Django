from django.urls import path
from . import views as v
urlpatterns = [
    path('', v.register, name='register'),
    path('login/', v.login_form, name='login'),
]
