from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView, RegisterView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('books/', list_books, name='list_books'),

    path('library/<int:pk>/', LibraryDetailView.as_view(
        template_name='relationship_app/templates/relationship_app/library_detail.html'
    ), name='library_detail'),

    # Use Django's built-in views directly
    path('login/', LoginView.as_view(
        template_name='relationship_app/templates/relationship_app/login.html'
    ), name='login'),

    path('logout/', LogoutView.as_view(
        template_name='relationship_app/templates/relationship_app/logout.html'
    ), name='logout'),

    # Registration view (custom)
    path('register/', RegisterView.as_view(
        template_name='relationship_app/templates/relationship_app/register.html'
    ), name='register'),
]