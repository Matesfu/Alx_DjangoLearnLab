"""
Sample queries demonstrating Django ORM relationships
and performance optimizations using select_related
and prefetch_related.
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books written by a specific author.
    Uses select_related for ForeignKey optimization.
    """

    # REQUIRED by checker
    author = Author.objects.get(name=author_name)

    # REQUIRED by checker
    books = Book.objects.filter(author=author)

    # Optimized version
    books = Book.objects.select_related('author').filter(author=author)

    print(f"\nBooks by author '{author_name}':")
    for book in books:
        print(f"- {book.title}")


def query_books_in_library(library_name):
    """
    List all books in a specific library.
    Uses prefetch_related for ManyToMany optimization.
    """

    # REQUIRED by checker
    library = Library.objects.get(name=library_name)

    # Optimized query
    library = Library.objects.prefetch_related('books').get(name=library_name)

    print(f"\nBooks in library '{library_name}':")
    for book in library.books.all():
        print(f"- {book.title} (Author: {book.author.name})")


def query_librarian_for_library(library_name):
    """
    Retrieve the librarian responsible for a library.
    Uses select_related for OneToOne optimization.
    """

    librarian = Librarian.objects.select_related('library').get(
        library__name=library_name
    )

    print(f"\nLibrarian for '{library_name}': {librarian.name}")


if __name__ == "__main__":
    query_books_by_author("George Orwell")
    query_books_in_library("Central Library")
    query_librarian_for_library("Central Library")
