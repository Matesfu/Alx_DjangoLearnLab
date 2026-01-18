from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

#Function-Based View
def list_books(request):
    """
    List all books stored in the database.
    """
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

#Class-Based View
class LibraryDetailView(DetailView):
    """
    Display details of a specific library and its books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
