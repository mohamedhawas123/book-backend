from rest_framework import serializers
from .models import Author, Book, Page
from django.contrib.auth.models import User

class UserSerizlier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerizlier()
    class Meta:
        model = Author
        fields= '__all__'



class BookSerializer(serializers.ModelSerializer):
    author=serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = '__all__'




    def to_representation(self, instance):
        representation = super().to_representation(instance)
        author_data = AuthorSerializer(instance.author).data
        representation['author'] = author_data
        return representation




class PageSerializer(serializers.ModelSerializer):
    book=serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    

    class Meta:
        model = Page
        fields = '__all__'


    def to_representation(self,instance):
        represention =  super().to_representation(instance)
        book_data = BookSerializer(instance.book).data
        represention['book'] = book_data
        return represention

        