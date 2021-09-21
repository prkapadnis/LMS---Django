from collections import namedtuple
from django.contrib.auth import logout
from django.urls import path
from . import views
from registration import views as v
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-Book/', views.addBook, name='addBook'),
    path('view-books', views.viewBook, name='view-books'),
    path('register-student', views.registerStudent, name='register-student'),
    path('view-student-table', views.viewStudentTable, name='view-student-table'),
    path('issue-book-table', views.issueBookTable, name='issue-book-table'),
    path('view-student/<str:id>', views.viewStudent, name='view-student'),
    path('issue-book', views.issueBook, name='issue-book'),
    path('logout', v.logout_form, name='logout'),
    path('update-book/<str:id>', views.updateBook, name='update-book'),
    path('delete-book/<str:id>', views.deleteBook, name='delete-Book'),

]
