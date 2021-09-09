from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from . import models


class AddBookForm(ModelForm):
    class Meta:
        model = models.AddBookModel
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'placeholder': 'Enter the Book Name'}),
            'author_name': forms.TextInput(attrs={'placeholder': 'Enter the author of the book'}),
            'category': forms.TextInput(attrs={'placeholder': 'Enter Category'}),
            'isbn_no': forms.TextInput(attrs={'placeholder': 'Enter ISBN number'}),
            'quantity': forms.TextInput(attrs={'placeholder': 'Enter Quantity of Books'}),
        }


class StudentForm(ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        labels = {
            'stud_name': 'Name',
            'stud_email': 'Email',
            'stud_branch': 'Branch',
            'stud_enrollmentNo': 'Enrollment No'
        }
        widgets = {
            'stud_name': forms.TextInput(attrs={'placeholder': 'Enter the Name'}),
            'stud_email': forms.TextInput(attrs={'placeholder': 'Enter Email '}),
            'stud_branch': forms.Select(attrs={'placeholder': 'Select Branch'}),
            'stud_enrollmentNo': forms.TextInput(attrs={'placeholder': 'Enter the Enrollement Number'}),
        }
