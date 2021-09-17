from django.contrib.auth import logout
from django.urls import path
from . import views
from registration import views as v
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-Book/', views.addBook, name='addBook'),
    path('view-books', views.viewBook, name='view-books'),
    path('register-student', views.registerStudent, name='register-student'),
    path('view-student', views.viewStudent, name='view-student'),
    path('issue-book', views.issueBook, name='issue-book'),
    path('logout', v.logout_form, name='logout'),
]
