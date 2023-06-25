from django.shortcuts import render
from rest_framework import viewsets
from  .models import Author, Book, Page
from .serializers import AuthorSerializer, BookSerializer, PageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated





class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.request.query_params.get("author_id")
        if author_id:
            return Book.objects.filter(author__id=author_id)
        return Book.objects.all()

    def create(self, request, *args, **kwargs):
        author_id = request.data.get("author")
        print(author_id)

        if not author_id:
            return Response({"error": "author_id is required"}, status=400)

        author = Author.objects.get(id=author_id)
        book = Book(author=author)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return super().create(request, *args, **kwargs)

    


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes= [IsAuthenticated]


    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        page_number = self.request.query_params.get('page_number', 1) 
        print(page_number)
        queryset = Page.objects.filter(book__id=book_id, number=page_number)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)

        
    
   



    
