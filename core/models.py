from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username




class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title



class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.IntegerField( blank=True, null=True)
    content = models.TextField(blank=True)





