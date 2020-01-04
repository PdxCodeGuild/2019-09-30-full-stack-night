from django.db import models
import uuid
from datetime import date 

from django.contrib.auth.models import User

class Book(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class BookInstance(models.Model):
    id= models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Unique ID for this particular book across the entire library')
    book = models.ForeignKey('book', on_delete = models.SET_NULL, null = True)
    borrower = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    due_back = models.DateField(null = True , blank = True)

    LOAN_STATUS = (
        ('o' , 'onloan'),
        ('a' , 'available'),
        ('r' , 'reserved'),
    )

    status =  models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'a',
        help_text = 'book availabilty',
        )

    class Meta:
        ordering = ['book']

    def __str__(self):
        return f'{self.id}, ({self.book.title})'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False