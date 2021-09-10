from django.db import models

branch = (
    ('Computer Engineering', 'Computer Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Entc', 'Entc'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
)


class AddBookModel(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200, choices=branch)
    isbn_no = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.book_name


class StudentModel(models.Model):
    stud_name = models.CharField(max_length=200)
    stud_email = models.EmailField()
    stud_branch = models.CharField(max_length=200, choices=branch)
    stud_enrollmentNo = models.IntegerField()

    def __str__(self):
        return self.stud_name


class IssueBookModel(models.Model):
    stud_name = models.ForeignKey(
        StudentModel, null=True, on_delete=models.SET_NULL)
    book_name = models.ForeignKey(
        AddBookModel, null=True, on_delete=models.SET_NULL)
    issue_date = models.DateField(
        auto_now_add=False, auto_now=False, null=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.stud_name)
