from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),

    path('library/<int:pk>/', views.LibraryDetailView.as_view(
        template_name='relationship_app/templates/relationship_app/library_detail.html'
    ), name='library_detail'),

    # Must literally use LoginView.as_view(template_name=...) here
    path('login/', LoginView.as_view(
        template_name='relationship_app/templates/relationship_app/login.html'
    ), name='login'),

    # Must literally use LogoutView.as_view(template_name=...) here
    path('logout/', LogoutView.as_view(
        template_name='relationship_app/templates/relationship_app/logout.html'
    ), name='logout'),

    # Must literally reference views.register
    path('register/', views.RegisterView.as_view(
        template_name='relationship_app/templates/relationship_app/register.html'
    ), name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
