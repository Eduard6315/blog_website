from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Post, Comment


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    post_id = serializers.IntegerField()

    def create(self, validated_data):
        comment_data = {
            'text': validated_data['text'],
            'post_id': validated_data['post_id']
        }
        return Comment.objects.create(**comment_data)

class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        token = self.context['request'].META.get('HTTP_AUTHORIZATION')  # Получение токена из заголовка запроса
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    token = serializers.JSONField(write_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        token = validated_data.pop('token', None)
        post = super().create(validated_data)
        post.token = token
        post.save()  # Сохраняем пост

        return post

class TokenSerializer(serializers.Serializer):
    token = serializers.JSONField(write_only=True)




class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        return data


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
