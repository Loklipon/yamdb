import random

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from http import HTTPStatus
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from .exceptions import SendMailProblem
from .models import User
from .permissions import AuthAdminSuperUserPermission
from .serializers import (SignUpSerializer,
                          CreateTokenSerializer, UsersSerializer)


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get('username') == 'me':
                return Response(serializer.errors,
                                status=HTTPStatus.BAD_REQUEST)
            confirmation_code = random.randint(1, 1000000)
            email = serializer.validated_data.get('email')
            try:
                send_mail('Confirm your e-mail address',
                          f'Code: {confirmation_code}',
                          'Team YaMDb',
                          (f'{email}',))
            except SendMailProblem:
                raise SendMailProblem(
                    'Ошибка отправки письма с подтверждением')
            serializer.save()
            username = request.data.get('username')
            user = User.objects.get(username=username)
            user.mail_confirmation_code = confirmation_code
            user.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


class CreateTokenView(APIView):
    def post(self, request):
        serializer = CreateTokenSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            confirmation_code = serializer.data.get('mail_confirmation_code')
            user = get_object_or_404(User, username=username)
            if confirmation_code != user.mail_confirmation_code:
                return Response(serializer.errors,
                                status=HTTPStatus.BAD_REQUEST)
            token = RefreshToken.for_user(user)
            return Response({'token': str(token.access_token)},
                            status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'username'
    permission_classes = (AuthAdminSuperUserPermission, )

    @action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=(permissions.IsAuthenticated, ),
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = UsersSerializer(request.user)
            return Response(serializer.data, status=HTTPStatus.OK)
        if request.method == 'PATCH':
            serializer = UsersSerializer(request.user,
                                         data=request.data,
                                         partial=True)
            if serializer.is_valid():
                if request.user.role == 'user':
                    serializer.validated_data['role'] = 'user'
                serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
