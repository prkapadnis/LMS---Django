from django.db import models


class AddBookModel(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    isbn_no = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.book_name


branch = (
    ('Computer Engineering', 'Computer Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Entc', 'Entc'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
)


class StudentModel(models.Model):
    stud_name = models.CharField(max_length=200)
    stud_email = models.EmailField()
    stud_branch = models.CharField(max_length=200, choices=branch)
    stud_enrollmentNo = models.IntegerField()

    def __str__(self):
        return self.stud_name
