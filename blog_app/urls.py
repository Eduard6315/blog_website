from django.urls import path
from .views import  (
    CommentCreateAPIView, UserLoginView,
    RegistrationView, CustomTokenRefreshView, PostListAPIView,
    PostCreateAPIView, PostDeleteAPIView, PostDetailAPIView,
)

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('posts/delete/<int:postId>/', PostDeleteAPIView.as_view(), name='post-delete'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:postId>/comments/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),


]