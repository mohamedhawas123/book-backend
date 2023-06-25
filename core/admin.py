from django.contrib import admin
from .models import Author, Page, Book
# Register your models here.


admin.site.register(Author)
admin.site.register(Page)
admin.site.register(Book)