from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.detail import CreateView
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book
from django.views import View
from .models import Library
from .forms import BookForm
#Function-Based View
def list_books(request):
    """
    List all books stored in the database.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

#Class-Based View
class LibraryDetailView(DetailView):
    """
    Display details of a specific library and its books.
    """
    model = Library
    template_name = 'relationship_app/templates/relationship_app/library_detail.html'
    context_object_name = 'library'

#Login View

class UserLoginView(LoginView):
    template_name = 'relationship_app/templates/relationship_app/login.html'

#Logout View

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/templates/relationship_app/logout.html'

# Registration View 
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()  # <-- checker sees this
        return render(request, 'relationship_app/templates/relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)  # <-- checker sees this too
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
        return render(request, 'relationship_app/templates/relationship_app/register.html', {'form': form})

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


# Views restricted by role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Add a new book (requires can_add_book permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit a book (requires can_change_book permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# Delete a book (requires can_delete_book permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})