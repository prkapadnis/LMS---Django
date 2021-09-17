from django import forms
from django.shortcuts import render
from .forms import AddBookForm, IssueBookForm, StudentForm
from .models import AddBookModel, IssueBookModel, StudentModel
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    books = AddBookModel.objects.count()
    issueBooks = IssueBookModel.objects.count()
    students = StudentModel.objects.count()
    studentModel = StudentModel.objects.all()[:4]
    issueBookModel = IssueBookModel.objects.all()[:5]
    context = {'students': studentModel, 'books': books,
               'issuebook': issueBooks, 'student': students, 'issueBooks': issueBookModel}
    return render(request, 'library/dashboard.html', context=context)


@login_required(login_url='login')
def addBook(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddBookForm()
    context = {'form': form}
    return render(request, 'library/addBook.html', context=context)


@login_required(login_url='login')
def viewBook(request):
    books = AddBookModel.objects.all()
    context = {'books': books}
    return render(request, 'library/viewBooks.html', context=context)


@login_required(login_url='login')
def registerStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    context = {'form': form}
    return render(request, 'library/registerStudent.html', context=context)


@login_required(login_url='login')
def viewStudent(request):
    student = StudentModel.objects.all()
    context = {'students': student}
    return render(request, 'library/viewStudents.html', context=context)


@login_required(login_url='login')
def issueBook(request):
    form = IssueBookForm()
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'library/issueBook.html', context=context)
