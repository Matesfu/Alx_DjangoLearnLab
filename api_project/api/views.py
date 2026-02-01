from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        # 1. Start with the base list of all books
        queryset = super().get_queryset() 
        
        # 2. Look for '?title=...' in the URL
        title_filter = self.request.query_params.get('title', None)
        author_filter = self.request.query_params.get('author', None)
        # 3. If the user provided a title, narrow down the results
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)
        if author_filter is not None:
            queryset = queryset.filter(author__icontains=author_filter)    
        return queryset

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]