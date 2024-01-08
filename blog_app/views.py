from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .models import Post, Comment
from .serializers import (
    PostSerializer, CommentSerializer, UserLoginSerializer,
    RegistrationSerializer,
    TokenSerializer, PostDetailSerializer
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostCreateAPIView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        token = request.data.get('token')
        user = request.user


        if user.is_superuser and token is not None:
            from rest_framework_simplejwt.tokens import AccessToken
            try:
                AccessToken(token)  # Попытка создать AccessToken из предоставленного токена
            except Exception as e:
                return Response('Неверный токен', status=status.HTTP_401_UNAUTHORIZED)

            # Проверка разрешений пользователя
            if user.has_perm('blog_app.can_add_post'):
                serializer = PostSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Недостаточно прав', status=status.HTTP_403_FORBIDDEN)

        return Response('Недостаточно прав или неверный токен', status=status.HTTP_403_FORBIDDEN)


class PostDeleteAPIView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)


    def delete(self, request, postId):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.data.get('token')
        user = request.user

        if user.is_superuser and token is not None:
            try:
                AccessToken(token)
            except Exception as e:
                return Response('Неверный токен', status=status.HTTP_401_UNAUTHORIZED)

            # Проверка разрешений пользователя
            if user.has_perm('blog_app.can_delete_post'):
                try:
                    post = Post.objects.get(pk=postId)
                    post.delete()
                    return Response('Пост успешно удален', status=status.HTTP_204_NO_CONTENT)
                except Post.DoesNotExist:
                    return Response('Пост не найден', status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('Недостаточно прав для удаления поста', status=status.HTTP_403_FORBIDDEN)

        return Response('Недостаточно прав или неверный токен', status=status.HTTP_403_FORBIDDEN)


class PostDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'  # Обновить эту строку на 'pk'



class CommentCreateAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, postId):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment_data = {
                'text': serializer.validated_data['text'],
                'post_id': postId
            }
            comment = Comment.objects.create(**comment_data)
            return Response(
                {"text": comment.text},
                status=201
            )
        return Response(serializer.errors, status=400)



class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # Валидация прошла успешно
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User.objects.get(username=username)
            if check_password(password, user.password):
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                request.session['access_token'] = access_token
                response_data = {
                    'message': 'Авторизация прошла успешно!',
                    'username': username,
                    'token': access_token,
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                error_data = {
                    'message': 'Неверные учетные данные',
                }
                return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


