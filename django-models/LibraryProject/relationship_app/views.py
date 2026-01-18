from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.detail import CreateView
from .models import Book
from .models import Library

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

#Registration View

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/templates/relationship_app/register.html'
    success_url = reverse_lazy('list_books')  # Redirect after registration

    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)
        # Log in the newly registered user
        login(self.request, self.object)
        return response
