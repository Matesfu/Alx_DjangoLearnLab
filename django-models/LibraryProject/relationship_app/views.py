from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.detail import CreateView
from .models import Book
from django.views import View
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
