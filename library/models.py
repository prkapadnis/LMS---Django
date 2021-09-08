from typing import ClassVar
from django.db import models


class AddBookModel(models.Model):
    book_name = models.CharField(max_length=200,)
    author_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    isbn_no = models.IntegerField()
    quantity = models.IntegerField()
    

    def __str__(self):
        return self.book_name
