## Book API Views

This project uses Django REST Framework generic views to handle CRUD operations
for the Book model.

### Endpoints
- GET /api/books/ → List all books (public)
- GET /api/books/<id>/ → Retrieve a book (public)
- POST /api/books/create/ → Create a book (authenticated users)
- PUT /api/books/<id>/update/ → Update a book (authenticated users)
- DELETE /api/books/<id>/delete/ → Delete a book (authenticated users)

### Permissions
- Read-only access is allowed for unauthenticated users.
- Write operations require authentication.

### Validation
- Book publication year cannot be in the future.

## Book API: Filtering, Searching, and Ordering

The `/api/books/` endpoint supports advanced query capabilities:

### 1. Filtering
You can filter books by exact matches of specific fields:

- **title**: Filter by book title.
- **author__name**: Filter by the name of the author (follows the ForeignKey relationship).
- **publication_year**: Filter by the year the book was published.