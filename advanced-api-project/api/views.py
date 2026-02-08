from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book, Author
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # fields users can filter by
    search_fields = ['title', 'author__name']  # fields to search in
    ordering_fields = ['title', 'publication_year']  # fields allowed for ordering
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a single book by ID.
    Accessible to both authenticated and unauthenticated users.
    advanced query capabilities: filtering, searching, and ordering.
    
    Features:
    1. Filtering:
       - Users can filter books by exact field matches.
       - Supported fields: 'title', 'author__name', 'publication_year'
       - Example: GET /api/books/?title=1984
       - Example: GET /api/books/?author__name=George+Orwell
       - Example: GET /api/books/?publication_year=1949

    2. Searching:
       - Users can perform text searches on specified fields.
       - Searchable fields: 'title', 'author__name'
       - Example: GET /api/books/?search=Harry+Potter

    3. Ordering:
       - Users can order results by any allowed field.
       - Supported fields: 'title', 'publication_year'
       - Example: GET /api/books/?ordering=publication_year
       - Example: GET /api/books/?ordering=-title
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
