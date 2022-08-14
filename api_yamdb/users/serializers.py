from rest_framework import serializers
import re

from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        regex = re.compile('^[a-z][a-z0-9_]+$')
        username = data.get('username')
        email = data.get('email')
        if not regex.search(username):
            raise serializers.ValidationError(
                'Недопустимое имя пользователя')
        if username == 'me':
            raise serializers.ValidationError(
                'Имя пользователя не может быть "me"')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует')
        return data


class CreateTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'mail_confirmation_code')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
