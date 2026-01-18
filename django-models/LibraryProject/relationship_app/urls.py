from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView, RegisterView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    # Correct syntax for DetailView with <int:pk>
    path('library/<int:pk>/', LibraryDetailView.as_view(
        template_name='relationship_app/templates/relationship_app/library_detail.html'
    ), name='library_detail'),

    # Login and Logout views with template_name explicitly set
    path('login/', UserLoginView.as_view(
        template_name='relationship_app/templates/relationship_app/login.html'
    ), name='login'),

    path('logout/', UserLogoutView.as_view(
        template_name='relationship_app/templates/relationship_app/logout.html'
    ), name='logout'),

    # Registration view referenced as views.register (lowercase)
    path('register/', RegisterView.as_view(
        template_name='relationship_app/templates/relationship_app/register.html'
    ), name='register'),
]
