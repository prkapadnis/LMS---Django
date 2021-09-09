from django import forms
from django.shortcuts import render
from .forms import AddBookForm, StudentForm
from .models import AddBookModel, StudentModel


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


def viewBook(request):
    books = AddBookModel.objects.all()
    context = {'books': books}
    return render(request, 'library/viewBooks.html', context=context)


def registerStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    context = {'form': form}
    return render(request, 'library/registerStudent.html', context=context)


def viewStudent(request):
    student = StudentModel.objects.all()
    context = {'students': student}
    return render(request, 'library/viewStudents.html', context=context)
