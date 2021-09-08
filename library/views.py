from django import forms
from django.shortcuts import render
from .forms import AddBookForm


def index(request):
    context = {}
    return render(request, 'library/dashboard.html')


def addBook(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddBookForm()
    context = {'form': form}
    return render(request, 'library/addBook.html', context=context)
