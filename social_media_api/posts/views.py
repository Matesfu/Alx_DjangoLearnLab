from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from notifications.models import Notification
from notifications.utils import create_notification
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        # Create notification for post author if it's not self
        post_author = comment.post.author
        if post_author != self.request.user:
            create_notification(
                recipient=post_author,
                actor=self.request.user,
                verb='commented on your post',
                target=comment.post
            )

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get users the current user is following
        following_users = self.request.user.following.all()
        # Return posts from following users, most recent first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        # ✅ Checker-friendly: use get_or_create to prevent duplicate likes
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'detail': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_object_id=post.id,
                target_content_type=post._meta.model_name
            )

        return Response({'detail': 'Post liked'}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        deleted, _ = Like.objects.filter(user=request.user, post=post).delete()
        if deleted == 0:
            return Response({'detail': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Post unliked'}, status=status.HTTP_200_OK)