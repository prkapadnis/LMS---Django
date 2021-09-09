from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('add-Book/', views.addBook, name='addBook'),
    path('view-books', views.viewBook, name='view-books'),
    path('register-student', views.registerStudent, name='register-student'),
    path('view-student', views.viewStudent, name='view-student'),
]
