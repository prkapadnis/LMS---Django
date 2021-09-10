from django.contrib import admin
from . import models

admin.site.register(models.AddBookModel)
admin.site.register(models.StudentModel)
admin.site.register(models.IssueBookModel)
