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
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)
from .views import SearchResultsView, TagPostsView

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
]

urlpatterns += [

    # Create comment
    path(
        'post/<int:pk>/comments/new/',
        CommentCreateView.as_view(),
        name='comment-create'
    ),

    # Update comment
    path(
        'comment/<int:pk>/update/',
        CommentUpdateView.as_view(),
        name='comment-update'
    ),

    # Delete comment
    path(
        'comment/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment-delete'
    ),
]

urlpatterns += [

    path(
        'search/',
        SearchResultsView.as_view(),
        name='search'
    ),

    path(
        'tags/<str:tag_name>/',
        TagPostsView.as_view(),
        name='tag-posts'
    ),
]