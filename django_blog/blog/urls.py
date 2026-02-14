from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='blog/logout.html'
    ), name='logout'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('', views.home, name='home'),
    # path('posts/', views.posts, name='posts'),
    path('', PostListView.as_view(), name='post-list'),

    # Create
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Detail
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Update
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
