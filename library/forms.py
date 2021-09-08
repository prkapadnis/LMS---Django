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
