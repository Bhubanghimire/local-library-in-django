from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(Self):
        return Self.name



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField('ISBN',max_length=13)
    genre = models.ManyToManyField(Genre,help_text='enter genere for book')

    def display_genre(Self):
        return (',' .join(genre.name for genre in Self.genre.all()[:3]))
    def __str__(Self):
        return Self.title


    def get_absolute_url(self):
        return reverse('Book-detail',args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    LOAN_STATUS = (
        ('m','maintain'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1,
                            choices=LOAN_STATUS
    )

    


    class Meta:
        ordering = ['due_back']

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return f'{self.id} ({self.book.title})'



class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100,default="ghimire")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


