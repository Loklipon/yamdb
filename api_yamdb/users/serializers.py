from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


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
