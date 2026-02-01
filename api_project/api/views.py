from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        # 1. Start with the base list of all books
        queryset = super().get_queryset() 
        
        # 2. Look for '?title=...' in the URL
        title_filter = self.request.query_params.get('title', None)
        
        # 3. If the user provided a title, narrow down the results
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)
            
        return queryset

